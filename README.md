# Prompt2Query (NL2SQL SaaS)

Prompt2Query is a modern SaaS web application that empowers non-technical users to interact with their databases using natural language. Users can connect their own databases (PostgreSQL, MySQL), ask questions in plain English, and get instant SQL queries and results—no SQL knowledge required!

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

![Screenshot 2025-07-02 124210](https://github.com/user-attachments/assets/47bafd59-d470-4247-97a7-a6c9ed8e374c)


### Query with AI

![Screenshot 2025-07-02 124242](https://github.com/user-attachments/assets/df47e630-05d2-439b-949d-15d69411f950)

![Screenshot 2025-07-02 124445](https://github.com/user-attachments/assets/62c22891-c5ea-441d-9c7e-f004ba2fb709)


### Query History

![Screenshot 2025-07-02 124500](https://github.com/user-attachments/assets/41b4ad3b-a90a-4a4d-8247-ead25b5dac09)

### Database Overview

![Screenshot 2025-07-02 124524](https://github.com/user-attachments/assets/55d18670-c585-4b6b-a1ad-734ea3ec3215)

![Screenshot 2025-07-02 124228](https://github.com/user-attachments/assets/de2fc526-ab24-4e38-8619-e4a9b1628c78)

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

---

## ⚡ Example Use Case: Student Management System

Suppose you have a **Student Management System** database with tables like `students`, `courses`, `attendance`, etc.

- **Connect your database** (local or cloud PostgreSQL/MySQL).
- **Ask:**  
  - "List all students enrolled in B.Com from Delhi"
  - "Show attendance for student ADM033"
  - "How many students are hostellers?"
- **Get:**  
  - The exact SQL query and the results, instantly.

**Related Project:**  
- [Student Management System with NL2SQL (Demo & Source)](https://github.com/shaikabdulgaffar/SMS-NL2SQL)

---

## 🔗 Useful Links

- [Font Awesome Icons](https://fontawesome.com/)
- [Django Documentation](https://docs.djangoproject.com/)
- [Google Gemini API](https://ai.google.dev/gemini-api/docs)
---

## 🖥️ Local Setup

1. **Clone the repo:**
   ```bash
   git clone https://github.com/shaikabdulgaffar/Prompt2Query.git
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
> I’ve built this project to function like a SaaS product, allowing each user to securely connect their own database and run queries using natural language.
> I always welcome your feedback and suggestions!

---

## 📧 Contact & Contributions

- For issues, suggestions, or contributions, please open an issue or pull request on this repo.
- For business or demo requests, contact [shaikabdulgaffar01@gmail.com](mailto:shaikabdulgaffar01@gmail.com).

---

**Prompt2Query** – Unlock your data with the power of natural language!
