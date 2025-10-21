from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
import psycopg2
import psycopg2.extras
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'super-secret-key') 

# ----------------------------
# PostgreSQL Configuration
# ----------------------------
DATABASE_URL = os.environ.get("DATABASE_URL") or "postgresql://postgres:root@localhost:5432/smartcareer_db"

def get_db_connection():
    return psycopg2.connect(DATABASE_URL)

# ----------------------------
# Routes
# ----------------------------
@app.route('/')
def index():
    return render_template('index.html')

# ----------------------------
# Register user
# ----------------------------
@app.route('/add', methods=['POST'])
def add_user():
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email = request.form.get('email')
    password = request.form.get('password')
    role = request.form.get('role')
    class_role = request.form.get('class_role')  # Make sure form field matches column

    if not all([first_name, last_name, email, password, role, class_role]):
        flash("All fields are required!", "danger")
        return redirect(url_for('index'))

    hashed_pw = generate_password_hash(password)

    try:
        with get_db_connection() as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                cur.execute("""
                    INSERT INTO users (first_name, last_name, email, password, role, class_role)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """, (first_name, last_name, email, hashed_pw, role, class_role))
                conn.commit()
        flash("Registration successful!", "success")
    except Exception as e:
        print("Error inserting user:", e)
        flash("Something went wrong!", "danger")

    return redirect(url_for('login'))

# ----------------------------
# Login user
# ----------------------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if not all([email, password]):
            flash("Email and password required!", "danger")
            return redirect(url_for('login'))

        try:
            with get_db_connection() as conn:
                with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                    cur.execute("SELECT * FROM users WHERE email = %s", (email,))
                    user = cur.fetchone()
        except Exception as e:
            print("Database error:", e)
            flash("Database error!", "danger")
            return redirect(url_for('login'))

        if user:
            if check_password_hash(user['password'], password):
                # Example session usage
                session['user_id'] = user['id']
                session['email'] = user['email']
                flash("Login successful!", "success")
                return redirect(url_for('index'))
            else:
                flash("Incorrect password.", "danger")
        else:
            flash("User does not exist.", "warning")

    return render_template('login.html')

# ----------------------------
# Logout route
# ----------------------------
@app.route('/logout')
def logout():
    session.clear()
    flash("Logged out successfully.", "success")
    return redirect(url_for('index'))

# ----------------------------
if __name__ == '__main__':
    # Use environment PORT if deploying, else default 5000
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, port=port)
