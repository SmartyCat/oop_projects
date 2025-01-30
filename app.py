from flask import Flask, g, redirect, render_template, request
import sqlite3 as sq
from flask_login import LoginManager, login_required
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import (
    LoginManager,
    login_required,
    current_user,
    login_user,
    logout_user,
)
from UserLogin import UserLogin, UserMixin

DATABASE = "users.db"
SECRET_KEY = "1234qwer"

app = Flask(__name__)
app.config.from_object(__name__)

login_manager = LoginManager(app)


@login_manager.user_loader
def load_user(user_id):
    db = get_db()
    print("xuy")
    return UserLogin().fromDB(user_id, db)


def connect_db():
    conn = sq.connect(app.config["DATABASE"])
    return conn


def create_db():
    db = connect_db()
    with app.open_resource("users.sql", mode="r") as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


def get_db():
    if not hasattr(g, "link_db"):
        g.link_db = connect_db()
    return g.link_db


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, "link_db"):
        g.link_db.close()


@app.route("/")
def index():
    if current_user.is_authenticated:
        return redirect("profile")
    return render_template("index.html")


@app.route("/registr", methods=["POST", "GET"])
def registr():
    db = get_db()
    if request.method == "POST":
        if request.form.get("email") and request.form.get(
            "password"
        ) == request.form.get("password2"):
            db.cursor().execute(
                "INSERT INTO users VALUES(Null,?,?)",
                (
                    request.form.get("email"),
                    generate_password_hash(request.form.get("password")),
                ),
            )
            db.commit()
    return render_template("registr.html")




@app.route("/login", methods=["POST", "GET"])
def login():
    db = get_db()
    if request.method == "POST":
        email = request.form.get("email_login")
        user = (
            db.cursor()
            .execute("SELECT * FROM users WHERE email=? LIMIT 1", (email,))
            .fetchone()
        )
        if user and check_password_hash(user[2], request.form.get("password_login")):
            userlogin = UserLogin().create(user)
            login_user(userlogin)
            return redirect("/")
    return render_template("login.html")


@app.route("/profile")
def profile():
    db = get_db()
    email=db.cursor().execute("SELECT email FROM users WHERE id = ? LIMIT 1",(current_user.get_id(),)).fetchone()
    return render_template("profile.html",email=email[0])


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/")
