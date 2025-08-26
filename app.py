import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
import re
from chatbot import get_bot_response

def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

app = Flask(__name__)
app.secret_key = "secretkey"   # for flash messages and sessions

@app.route("/")
def index():
    return render_template("index.html")

# ------------------- SIGNUP -------------------
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        name = request.form["name"]
        worker_id = request.form["worker_id"]
        department = request.form["department"]
        email = request.form["email"]
        password = request.form["password"]
        confirm = request.form["confirm"]

        # Password confirmation
        if password != confirm:
            flash("Passwords do not match!", "danger")
            return render_template("signup.html", name=name, worker_id=worker_id,
                                   department=department, email=email)

        # Email must be @high5.com
        if not re.match(r"^[^@]+@high5\.com$", email):
            flash("Email must be a @high5.com address", "danger")
            return render_template("signup.html", name=name, worker_id=worker_id,
                                   department=department)

        # Password strength check
        if len(password) <= 5 or not re.search(r"\d", password) or not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            flash("Password must be > 5 characters and include at least one number and one symbol", "danger")
            return render_template("signup.html", name=name, worker_id=worker_id,
                                   department=department, email=email)

        conn = get_db_connection()

        # Check duplicate worker_id
        existing_worker = conn.execute(
            "SELECT * FROM users WHERE worker_id = ?", (worker_id,)
        ).fetchone()
        if existing_worker:
            flash("Worker ID already exists!", "danger")
            conn.close()
            return render_template("signup.html", name=name, department=department, email=email)

        # Check duplicate email
        existing_email = conn.execute(
            "SELECT * FROM users WHERE email = ?", (email,)
        ).fetchone()
        if existing_email:
            flash("Email already exists!", "danger")
            conn.close()
            return render_template("signup.html", name=name, worker_id=worker_id, department=department)

        # Hash password and insert
        hashed_password = generate_password_hash(password)
        conn.execute(
            "INSERT INTO users (name, worker_id, department, email, password) VALUES (?, ?, ?, ?, ?)",
            (name, worker_id, department, email, hashed_password)
        )
        conn.commit()
        conn.close()

        flash("Signup successful! Please log in.", "success")
        return redirect(url_for("login"))

    return render_template("signup.html")


# ------------------- LOGIN -------------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        conn = get_db_connection()
        user = conn.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()
        conn.close()

        # Check if user exists and password matches
        if user and check_password_hash(user["password"], password):
            session["user_id"] = user["id"]
            session["user_name"] = user["name"]
            flash("Login successful!", "success")
            return redirect(url_for("chatbox"))
        else:
            flash("Invalid email or password", "danger")

    return render_template("login.html")

# ------------------- CHATBOX -------------------
@app.route("/chatbox", methods=["GET", "POST"])
def chatbox():
    if "user_id" not in session:
        flash("Please log in to access the chatbox.", "danger")
        return redirect(url_for("login"))

    if "messages" not in session:
        session["messages"] = []

    if request.method == "POST":
        question = request.form["question"]

        # Save user message
        session["messages"].append({
            "username": session["user_name"],
            "text": question
        })

        # Call chatbot 
        answer = get_bot_response(question) or "I didn’t quite get that."

        # Save bot reply
        session["messages"].append({
            "username": "Bot",
            "text": answer
        })

        session.modified = True
        return redirect(url_for("chatbox"))

    return render_template("chatbox.html", user=session["user_name"], messages=session["messages"])

# ------------------- LOGOUT -------------------
@app.route("/logout")
def logout():
    session.clear()
    flash("You have been logged out.", "info")
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
