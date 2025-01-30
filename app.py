from flask import Flask,render_template,redirect,g,request,session
import sqlite3 as sq
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import LoginManager,login_user,login_required
from UserLogin import UserLogin


DATABASE="users.db"
SECRET_KEY="1234qwer"

app=Flask(__name__)
app.config.from_object(__name__)
login_manager=LoginManager(app)

@login_manager.user_loader
def load_user(user_id):
    db=get_db()
    print("pizda")
    return UserLogin().fromDB(user_id,db)

def connect_db():
    conn=sq.connect(app.config["DATABASE"])
    return conn

def create_db():
    db=connect_db()
    with app.open_resource("users.sql",mode="r") as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()

def get_db():
    if not hasattr(g,"link_db"):
        g.link_db=connect_db()
    return g.link_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g,"link_db"):
        g.link_db.close()

@app.route("/")
def index():
    db=get_db()
    return render_template("index.html")

@app.route("/registr",methods=["POST","GET"])
def registr():
    db=get_db()
    if request.method=="POST":
        email=request.form.get("email")
        password=request.form.get("password")
        password2=request.form.get("password2")
        if email and password==password2:
            password=generate_password_hash(password)
            db.cursor().execute("INSERT INTO users VALUES(Null,?,?)",(email,password))
            db.commit()
            return redirect("/")
    return render_template("registr.html")

@app.route("/login",methods=["POST","GET"])
def login():
    db=get_db()
    if request.method=="POST":
        email_login=request.form.get("email_login")
        user=db.cursor().execute("SELECT * FROM users WHERE username = ?",(email_login,)).fetchall()
        if user[0][1] and check_password_hash(user[0][2],request.form.get("password_login")):
            userlogin=UserLogin().create(user[0])
            login_user(userlogin)
            return redirect("/gold")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@app.route("/gold")
@login_required
def gold():
    return render_template("gold.html")

