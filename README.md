# High5 Onboarding Chatbot
- **Project**: Conversational Onboarding Platform for High5 New Hires

## Team Members
- Vaenesa Gayatri (Leader)       - develop chatbot
- Chan Hew Yan                   - develop chatbot
- Chook Yao Yu                   - develop applicants' career site, and recruitment portal
- Shirlyn Chew Ming Huey         - develop applicants' career site, and recruitment portal
- Muhammad Rasuli Bin Akbar Ali  - survey

## Problem and Solution Summary

### Scenario - Company Background
High5 is a small-to-medium IT services company based in Kuala Lumpur with around 60 employees. They specialize in providing cloud infrastructure, cybersecurity solutions, and custom software development for SMEs. The company is growing rapidly and needs to expand its workforce, especially in software engineering, data analysis, and cybersecurity.

### Problem Statement
In many organizations, employees face difficulties accessing HR, finance, and IT-related information quickly. Common processes such as leave applications, financial claims, travel requests, and IT equipment requisitions often require navigating multiple portals, reading lengthy policy documents, or waiting for HR/IT responses.

This leads to:
- Wasted time searching for the right forms and procedures
- Confusion due to scattered or unclear documentation
- Reduced productivity as employees depend on manual assistance
- Limited accessibility outside working hours
  
There is a need for a centralized, intelligent, and user-friendly system that allows employees to:
- Securely log in with their credentials
- Instantly get step-by-step guidance on organizational processes
- Access HR/IT/Finance support 24/7 through a chatbot interface
- Ensure secure handling of user data and conversations
The Employee Support Chatbot Portal addresses these issues by combining Flask web authentication with an NLTK-powered chatbot, creating a seamless and efficient self-service solution for employees.

### Solution Overview
The Employee Support Chatbot Portal is an internal HR and IT support system designed to streamline employee requests and provide instant guidance via an AI-powered chatbot.

It integrates:
- **Authentication & User Management** : Secure signup/login with validation and password hashing
- **Chatbot Assistance** : NLTK-powered chatbot that guides employees through HR, finance, and IT processes
- **Process Guidance** : Automated, step-by-step instructions for leave applications, claims, equipment requests, and more
- **Secure Data Handling** : SQLite database for user management and session tracking

### Key Features

- **AI Chatbot** : Provides instant responses to HR/IT/Finance queries
- **User Authentication** : Signup/login system with password strength validation
- **Database Management** : SQLite-based user storage with worker ID & department tracking
- **Process Automation** : Automated responses with step-by-step workflow guidance
- **Responsive UI** : Flask templates for signup, login, chat, and dashboard
- **Session Tracking** : Conversation history stored per session

## Technology Stack

### Frontend
- **Flask Templates (Jinja2)** – HTML rendering (index.html, signup.html, login.html, chatbox.html, base.html, chat.html)
- **Bootstrap / CSS** – Styling and layout (if applied)

### Backend
- **Python 3.9+** – Core language
- **Flask**– Web framework
- **Werkzeug Security**** – Password hashing & verification
- **SQLite3** – Lightweight relational database
- **NLTK** – Natural Language Toolkit for chatbot responses

### Development Tools
- **schema.sql** – Database schema definition
- **init_db.py** – Database initialization script
- **app.py** – Main Flask application
- **chatbot.py** – Chatbot logic and response patterns

### Project Structure
├── app.py              # Main Flask application  
├── chatbot.py          # Chatbot logic  
├── database.db         # SQLite database file  
├── init_db.py          # Script to initialize database  
├── schema.sql          # Database schema  
├── templates/          # HTML templates  
│   ├── base.html  
│   ├── index.html  
│   ├── login.html  
│   ├── signup.html  
│   ├── chatbox.html  
│   └── chat.html  

## Setup Instructions
Prerequisites
- **Python 3.9+**
- **pip** (Python package manager)
- **Virtual environment**

Installation
1. Clone repository
```powershell
# 1) Clone repository
git clone https://github.com/vaen0001-dot/High5.git
cd employee-support-chatbot

# 2) Create & activate virtual environment
python -m venv venv
# macOS/Linux
source venv/bin/activate
# Windows
# venv\Scripts\activate

# 3) Install dependencies
pip install -r requirements.txt
```

2. Database Setup
2.1 Initialize the database
```powershell
# Use the provided script to create the users table:
python init_db.py

# (Manual alternative in Python REPL:)
import sqlite3
conn = sqlite3.connect("database.db")
conn.execute("""
CREATE TABLE IF NOT EXISTS users (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
worker_id TEXT NOT NULL UNIQUE,
department TEXT NOT NULL,
email TEXT NOT NULL UNIQUE,
password TEXT NOT NULL
);
""")
conn.commit(); conn.close()
```

3. Run the app:
```powershell
python app.py
```

4. Open the app in your browser:
```powershell
http://127.0.0.1:5000
# Login domain rule: signup enforces emails ending with @high5.com. Passwords must be > 5 chars and include at least one number and one symbol.
```

5. (Optional) NLTK Data
```powershell
import nltk
nltk.download('punkt'); nltk.download('wordnet'); nltk.download('omw-1.4')
```

## Usage Guide

### User Signup
- Navigate to /signup
- Enter details (must use @high5.com email)
- Password must include a number & symbol
- Confirm password → account created

### User Login
- Navigate to /login
- Enter registered email and password
- On success → redirected to chatbot

### Chatbot Interaction
- Ask: leave application, financial claim, meeting room booking, it equipment request, etc.
- The bot returns step‑by‑step guidance
- Say quit or goodbye → ends session & redirects to homepage

## Security Notes
- Passwords are hashed using Werkzeug (generate_password_hash / check_password_hash)
- Sessions and flash messages use Flask’s secret key for production, set a strong key via env var and avoid committing secrets
- Inputs are validated for email domain and password strength

## Production Tips
- Use a real secret key via env (e.g., FLASK_SECRET_KEY)
- Serve behind a production WSGI server (e.g., Gunicorn) and reverse proxy
- Consider migrating to PostgreSQL/MySQL for multi‑user scale and backups
- 
## Reflection on Challenges and Learnings
### Technical Challenges
- **Database Management** – Structuring user authentication with SQLite
- **Password Security** – Implementing password hashing & validation
- **Chatbot Response Patterns** – Designing regex-based patterns with NLTK

### Key Learnings
- Flask routing, sessions, and flash messages
- Secure authentication & session handling
- Natural language processing basics with NLTK

### Future Improvements
- Migrate to PostgreSQL/MySQL for production use
- Add admin dashboard to manage users & processes
- Train chatbot with advanced NLP (spaCy / transformers)
- Deploy app on Docker/Heroku for real-world use

