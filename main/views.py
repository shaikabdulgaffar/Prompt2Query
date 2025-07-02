from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import DatabaseConnectionForm, NLQueryForm
from .models import DatabaseConnection, QueryHistory
from .nlp import nl_to_sql
import psycopg2
import MySQLdb
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import sqlite3
from rapidfuzz import process, fuzz
from google.api_core.exceptions import ResourceExhausted
from django.views.decorators.http import require_POST

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid credentials.")
    return render(request, "main/login.html")

def logout_view(request):
    logout(request)
    return redirect("login")

@login_required
def dashboard(request):
    dbs = DatabaseConnection.objects.filter(user=request.user)
    return render(request, "main/dashboard.html", {"dbs": dbs})

@login_required
def db_connect(request):
    if request.method == "POST":
        form = DatabaseConnectionForm(request.POST)
        if form.is_valid():
            db_conn = form.save(commit=False)
            db_conn.user = request.user
            db_conn.save()
            messages.success(request, "Database connection saved!")
            return redirect("dashboard")
    else:
        form = DatabaseConnectionForm()
    return render(request, "main/db_connect.html", {"form": form})

@login_required
def query(request, db_id):
    db_conn = DatabaseConnection.objects.get(id=db_id, user=request.user)
    result, sql_query = None, None
    error_message = None
    if request.method == "POST":
        form = NLQueryForm(request.POST)
        if form.is_valid():
            nl_query = form.cleaned_data["nl_query"]
            schema = get_table_schema(db_conn)
            course_values = ""
            if db_conn.db_type == "sqlite":
                conn = sqlite3.connect(db_conn.db_name)
                cursor = conn.cursor()
                try:
                    cursor.execute("SELECT DISTINCT course FROM students;")
                    rows = cursor.fetchall()
                    course_values = ", ".join([row[0] for row in rows])
                except Exception:
                    course_values = ""
                conn.close()
            try:
                sql_query = nl_to_sql(nl_query, schema, course_values, db_conn.db_type)
                result = execute_sql(db_conn, sql_query)
            except ResourceExhausted:
                error_message = (
                    "You have exceeded your daily Gemini API quota. "
                    "Please try again tomorrow or upgrade your Gemini API plan. "
                    "<a href='https://ai.google.dev/gemini-api/docs/rate-limits' target='_blank'>Learn more</a>."
                )
            except Exception as e:
                result = f"Error: {str(e)}"
            # Save history only if no quota error
            if not error_message:
                QueryHistory.objects.create(
                    user=request.user, db_conn=db_conn, nl_query=nl_query,
                    sql_query=sql_query, result=str(result)
                )
    else:
        form = NLQueryForm()
    return render(request, "main/query.html", {
        "form": form, "db_conn": db_conn, "result": result, "sql_query": sql_query, "error_message": error_message
    })

def get_table_schema(db_conn):
    if db_conn.db_type == "postgresql":
        conn = psycopg2.connect(
            host=db_conn.host, port=db_conn.port, user=db_conn.username,
            password=db_conn.password, dbname=db_conn.db_name
        )
        cur = conn.cursor()
        cur.execute("""
            SELECT table_name FROM information_schema.tables WHERE table_schema='public';
        """)
        tables = [row[0] for row in cur.fetchall()]
        schema = ""
        for table in tables:
            cur.execute(f"SELECT column_name, data_type FROM information_schema.columns WHERE table_name='{table}';")
            columns = cur.fetchall()
            schema += f"Table: {table}\nColumns: " + ", ".join(f"{col[0]} ({col[1]})" for col in columns) + "\n"
        conn.close()
        return schema
    elif db_conn.db_type == "mysql":
        conn = MySQLdb.connect(
            host=db_conn.host, port=db_conn.port, user=db_conn.username,
            passwd=db_conn.password, db=db_conn.db_name
        )
        cur = conn.cursor()
        cur.execute("SHOW TABLES;")
        tables = [row[0] for row in cur.fetchall()]
        schema = ""
        for table in tables:
            cur.execute(f"DESCRIBE {table};")
            columns = cur.fetchall()
            schema += f"Table: {table}\nColumns: " + ", ".join(col[0] for col in columns) + "\n"
        conn.close()
        return schema
    elif db_conn.db_type == "sqlite":
        conn = sqlite3.connect(db_conn.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = [row[0] for row in cursor.fetchall()]
        schema = ""
        for table in tables:
            cursor.execute(f"PRAGMA table_info({table});")
            columns = cursor.fetchall()
            schema += f"Table: {table}\nColumns: " + ", ".join(f"{col[1]} ({col[2]})" for col in columns) + "\n"
        conn.close()
        return schema
    return ""

def execute_sql(db_conn, sql_query):
    if db_conn.db_type == "postgresql":
        conn = psycopg2.connect(
            host=db_conn.host, port=db_conn.port, user=db_conn.username,
            password=db_conn.password, dbname=db_conn.db_name
        )
        cur = conn.cursor()
        cur.execute(sql_query)
        if cur.description:
            columns = [desc[0] for desc in cur.description]
            rows = cur.fetchall()
        else:
            columns, rows = [], []
        conn.commit()
        conn.close()
        return {"columns": columns, "rows": rows}
    elif db_conn.db_type == "mysql":
        conn = MySQLdb.connect(
            host=db_conn.host, port=db_conn.port, user=db_conn.username,
            passwd=db_conn.password, db=db_conn.db_name
        )
        cur = conn.cursor()
        cur.execute(sql_query)
        if cur.description:
            columns = [desc[0] for desc in cur.description]
            rows = cur.fetchall()
        else:
            columns, rows = [], []
        conn.commit()
        conn.close()
        return {"columns": columns, "rows": rows}
    return {}

@login_required
def query_history(request, db_id):
    db_conn = DatabaseConnection.objects.get(id=db_id, user=request.user)
    history = QueryHistory.objects.filter(user=request.user, db_conn=db_conn).order_by('-created_at')
    return render(request, "main/history.html", {"queries": history, "db_conn": db_conn})

@csrf_exempt
def generate_sql_view(request):
    if request.method == "POST":
        nl_query = request.POST.get("nl_query")
        table_schema = request.POST.get("table_schema")
        sql_query = nl_to_sql(nl_query, table_schema)
        return JsonResponse({"sql_query": sql_query})
    return JsonResponse({"error": "Invalid request"}, status=400)

from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import DatabaseConnection  # Apne model ka naam yahan use karein

@login_required
def db_delete(request, db_id):
    db = get_object_or_404(DatabaseConnection, id=db_id, user=request.user)
    if request.method == "POST":
        db.delete()
        messages.success(request, "Database connection removed successfully.")
        return redirect('dashboard')
    messages.error(request, "Invalid request.")
    return redirect('dashboard')

def get_closest_course(user_input, db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT course FROM students;")
    courses = [row[0] for row in cursor.fetchall()]
    conn.close()
    # Fuzzy match
    match, score, _ = process.extractOne(user_input, courses, scorer=fuzz.ratio)
    if score > 60:  # threshold, adjust as needed
        return match
    return user_input  # fallback

def generate_sql_for_student_names(user_input, db_path):
    # Fuzzy match course name
    closest_course = get_closest_course(user_input, db_path)
    # Always use case-insensitive match
    sql = f"SELECT name FROM students WHERE LOWER(course) = LOWER('{closest_course}');"
    return sql

# Example usage in your query view:
def query_view(request):
    # ...existing code...
    if request.method == "POST":
        nl_query = request.POST.get("nl_query")
        # Suppose you parse out the course name from nl_query as `course_name`
        # For demo, let's say:
        course_name = "b.com"  # Extracted from NL query
        db_path = "c:\\Users\\ag233\\Projects\\only nl2sql\\saas_nl2sql\\db.sqlite3"
        sql_query = generate_sql_for_student_names(course_name, db_path)
        # ...run sql_query and return results...

@require_POST
@login_required
def clear_history(request, db_id):
    db_conn = get_object_or_404(DatabaseConnection, id=db_id, user=request.user)
    QueryHistory.objects.filter(user=request.user, db_conn=db_conn).delete()
    messages.success(request, "Query history cleared successfully.")
    return redirect('history', db_id=db_id)

@login_required
def db_overview(request, db_id):
    db_conn = get_object_or_404(DatabaseConnection, id=db_id, user=request.user)
    overview = []
    if db_conn.db_type == "postgresql":
        import psycopg2
        conn = psycopg2.connect(
            host=db_conn.host, port=db_conn.port, user=db_conn.username,
            password=db_conn.password, dbname=db_conn.db_name
        )
        cur = conn.cursor()
        cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public';")
        tables = [row[0] for row in cur.fetchall()]
        for table in tables:
            cur.execute(f"SELECT column_name, data_type FROM information_schema.columns WHERE table_name='{table}';")
            columns = cur.fetchall()
            cur.execute(f"SELECT COUNT(*) FROM {table};")
            row_count = cur.fetchone()[0]
            cur.execute(f"SELECT * FROM {table} LIMIT 3;")
            sample = cur.fetchall()
            overview.append({
                "table": table,
                "columns": columns,
                "row_count": row_count,
                "sample": sample,
            })
        conn.close()
    # Add similar logic for MySQL and SQLite if needed
    return render(request, "main/db_overview.html", {"db_conn": db_conn, "overview": overview})