# Prompt2Query (NL2SQL SaaS)

Prompt2Query is a modern SaaS web application that empowers non-technical users to interact with their databases using natural language. Users can connect their own databases (PostgreSQL, MySQL, SQLite), ask questions in plain English, and get instant SQL queries and results—no SQL knowledge required!

---

## ✨ Features

- **Natural Language to SQL (NL2SQL):**  
  Type your question in plain English and get the corresponding SQL query and results.
- **Multi-Database Support:**  
  Connect PostgreSQL, MySQL, or SQLite databases (local or remote/cloud).
- **Database Overview:**  
  Instantly see all tables, columns, row counts, and sample data for any connected database.
- **Query History:**  
  View, search, and clear your past queries for each database.
- **Account Management:**  
  Secure login/logout, user-specific database connections and history.
- **Modern UI:**  
  Clean, responsive design with intuitive navigation and helpful feedback.
- **No Coding Required:**  
  Designed for end-users, business analysts, and anyone who wants insights from data without writing SQL.

---

## 📸 Screenshots

### Dashboard

![Dashboard Screenshot](screenshots/dashboard.png)

### Query with AI

![Query Page Screenshot](screenshots/query.png)

### Query History

![History Screenshot](screenshots/history.png)

### Database Overview

![Overview Screenshot](screenshots/overview.png)

---

## 🚀 How It Works

1. **Sign Up / Login:**  
   Create your account or log in.

2. **Connect a Database:**  
   - Click "Connect DB" and enter your database details (host, port, username, password, db name, type).
   - Supports remote PostgreSQL/MySQL servers (cloud or on-premise).

3. **Explore Database Overview:**  
   - Click "Overview" on any connected database card.
   - See all tables, columns, row counts, and sample data.

4. **Ask Questions in Natural Language:**  
   - Click "Query AI" on a database card.
   - Type your question (e.g., "List all students from Delhi").
   - The app generates and executes the SQL, showing both the query and results.

5. **View Query History:**  
   - Click "History" to see all your past queries for that database.
   - Clear history with one click.

6. **Account Management:**  
   - See your username and logout from the top bar.

---

## 🛠️ Tech Stack

- **Backend:** Django, Django ORM, psycopg2 (PostgreSQL), mysqlclient (MySQL), sqlite3
- **Frontend:** HTML5, CSS3, JavaScript, [Font Awesome](https://fontawesome.com/)
- **AI/NL2SQL:** Gemini 1.5 Flash API (Google)
- **Authentication:** Django Auth
- **Deployment:** Works on any server supporting Django (Heroku, AWS, DigitalOcean, etc.)

---

## ⚡ Example Use Case: Student Management System

Suppose you have a **Student Management System** database with tables like `students`, `courses`, `attendance`, etc.

- **Connect your database** (local or cloud PostgreSQL/MySQL/SQLite).
- **Ask:**  
  - "List all students enrolled in B.Com from Delhi"
  - "Show attendance for student ADM033"
  - "How many students are hostellers?"
- **Get:**  
  - The exact SQL query and the results, instantly.

**Related Project:**  
- [Student Management System with NL2SQL (Demo & Source)](https://github.com/saikiranboga/student-management-nl2sql-demo)

---

## 🔗 Useful Links

- [Font Awesome Icons](https://fontawesome.com/)
- [Django Documentation](https://docs.djangoproject.com/)
- [Google Gemini API](https://ai.google.dev/gemini-api/docs)
- [Student Management NL2SQL Demo Repo](https://github.com/saikiranboga/student-management-nl2sql-demo)

---

## 🖥️ Local Setup

1. **Clone the repo:**
   ```bash
   git clone https://github.com/yourusername/prompt2query.git
   cd prompt2query/saas_nl2sql
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment:**
   - Copy `.env.example` to `.env` and fill in your Gemini API key and Django secret key.

4. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (optional):**
   ```bash
   python manage.py createsuperuser
   ```

6. **Start the server:**
   ```bash
   python manage.py runserver
   ```

7. **Access the app:**  
   Open [http://localhost:8000](http://localhost:8000) in your browser.

---

## 📝 Notes

- **Remote Database Support:**  
  You can connect to any remote PostgreSQL/MySQL server (cloud or on-premise) as long as it allows external connections.
- **Security:**  
  All user data and database credentials are stored securely per Django best practices.
- **AI Quota:**  
  NL2SQL queries use Gemini API; ensure your API key has sufficient quota.

---

## 🚧 Project Status & Improvements

> **Note:**  
> Is project me abhi bhi kuch kamiya hain, jinhe resolve karne ke liye meri koshish jaari hai.  
> Main is project ko ek SaaS product jaisa banaya hai, taki har user apna database securely connect karke, natural language me queries kar sake.  
> Aapke feedback aur suggestions ka hamesha swagat hai!

---

## 📧 Contact & Contributions

- For issues, suggestions, or contributions, please open an issue or pull request on this repo.
- For business or demo requests, contact [your-email@example.com](mailto:your-email@example.com).

---

**Prompt2Query** – Unlock your data with the power of natural language!
