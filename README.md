# student_Reg_login_page_flask

A simple **user registration and login web application** built with **Flask** and **MySQL**. Users can register, log in securely, and passwords are hashed for safety.

---

## Features

- **User Registration**
  - New users can sign up with a username, email, and password.
  - Passwords are hashed using `Werkzeug` for security.

- **User Login**
  - Registered users can log in with their credentials.
  - Session management to maintain user login state.

- **Security**
  - Password hashing for safe storage.
  - Basic input validation to prevent common issues.

---

## Tech Stack

- **Backend:** Python, Flask
- **Database:** MySQL (via `Flask-MySQLdb`)
- **Frontend:** HTML, CSS, Bootstrap
- **Security:** Werkzeug for password hashing

---

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/flask-login-registration.git
   cd flask-login-registration

   Create a virtual environment (optional but recommended)

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows


Install dependencies

pip install -r requirements.txt


Configure MySQL database

Create a database in MySQL (e.g., user_db).

Update your Flask app config with your MySQL credentials:

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'user_db'


Run the Flask app

python app.py


Open http://127.0.0.1:5000 in your browser.

Folder Structure
flask-login-registration/
│
├── templates/        # HTML templates for login & registration
├── static/           # CSS, JS, images
├── app.py            # Main Flask application
├── requirements.txt  # Python dependencies
└── README.md         # Project documentation

Contribution

Contributions are welcome!

Fork the repo

Create a branch (git checkout -b feature-name)

Commit your changes (git commit -m "Add feature")

Push the branch (git push origin feature-name)

Open a Pull Request

License

MIT License

Author

Sai Kumar
Full Stack Developer


---

If you want, I can also **make a tiny visual demo section with screenshots of registration & login pages**—this makes your GitHub repo *look way more professional*.  

Do you want me to do that?

