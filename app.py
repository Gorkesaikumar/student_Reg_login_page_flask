from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
import MySQLdb.cursors
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'default-secret')


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''   
app.config['MYSQL_DB'] = 'smartcareer_db'

mysql = MySQL(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add', methods=['POST'])
def add_user():
    first = request.form['first_name']
    last = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    role = request.form['role']
    class_role = request.form['class_role']

    hashed_pw = generate_password_hash(password)

    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("""
        INSERT INTO users (first_name, last_name, email, password, role, class_name)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (first, last, email, hashed_pw, role, class_role))
    mysql.connection.commit()
    cur.close()

    return "Registration Sucessful" 


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Use DictCursor
        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = cur.fetchone()

        if user:
            stored_password = user['password']  

            if check_password_hash(stored_password, password):
                print(f"Entered password: '{password}'")
                print(f"Stored hash from DB: '{stored_password}'")
                print(len(stored_password))
                cur.close()
                return "Login successful!"
            else:
                cur.close()
                return "Incorrect password."
        else:
            cur.close()
            return "User does not exist."

    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
