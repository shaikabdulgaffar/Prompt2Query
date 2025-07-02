import os
import re
import google.generativeai as genai
from django.conf import settings

def clean_sql(sql):
    """
    Cleans the SQL output from LLM by removing markdown code fences and 'sql' labels.
    """
    # Remove starting code fence with 'sql' (```sql) or plain ```
    sql = re.sub(r"^```sql\s*", "", sql.strip(), flags=re.IGNORECASE)
    sql = re.sub(r"^```", "", sql.strip())
    # Remove ending code fence ```
    sql = re.sub(r"```$", "", sql.strip())
    # Remove any stray backticks
    sql = sql.strip().strip('`')
    return sql

def nl_to_sql(nl_query, table_schema, course_values=None, db_type=None):
    """
    Uses Gemini 1.5 Flash API to convert Natural Language query to SQL.
    """
    prompt = (
        "You are an expert SQL generator. "
        "Given the following database schema (all tables and columns):\n"
        f"{table_schema}\n"
        "If the user query contains spelling mistakes or partial names, use fuzzy matching to guess the correct column/table/value.\n"
    )
    if db_type == "sqlite":
        prompt += (
            "For SQLite, always use LOWER(column) LIKE LOWER('%value%') for case-insensitive matching. "
        )
    prompt += (
        "Return only the SQL query. Do not include explanation, markdown, or anything else.\n"
        "User Query: " + nl_query
    )
    genai.configure(api_key=settings.GEMINI_API_KEY)
    model = genai.GenerativeModel("models/gemini-1.5-flash-latest")
    response = model.generate_content(prompt)
    sql_query = response.text.strip()
    sql_query = clean_sql(sql_query)
    return sql_query