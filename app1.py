from flask import Flask,request,redirect,render_template,g,session
import sqlite3 as sq
from werkzeug.security import check_password_hash,generate_password_hash
from flask_login import LoginManager,login_required,login_user,current_user,logout_user
from UserLogin import UserLogin

DATABASE="users.db"
SECRET_KEY="1234qwer"
DEBUG=True

app=Flask(__name__)
app.config.from_object(__name__)
login_manager=LoginManager(app)
login_manager.login_view="login"

@login_manager.user_loader
def load_user(user_id):
    db=get_db()
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
    return render_template("index.html")

@app.route("/registr",methods=["POST","GET"])
def registr():
    db=get_db()
    if request.method=="POST":
        if request.form.get("username") and request.form.get("password")==request.form.get("password2"):
            db.cursor().execute("INSERT INTO users VALUES(Null,?,?)",(request.form.get("username"),generate_password_hash(request.form.get("password"))))
            db.commit()
            return redirect("/")
    return render_template("registr.html")

@app.route("/login",methods=["POST","GET"])
def login():
    if current_user.is_authenticated:
        return redirect("profile")
    db=get_db()
    if request.method=="POST":
        user=db.cursor().execute("SELECT username,password FROM users WHERE username = ?",(request.form.get("username_login"),)).fetchone()
        if request.form.get("username_login") and check_password_hash(user[1],request.form.get("password_login")):
            user_login=UserLogin().create(user)
            rm=True if request.form.get("remember") else False
            login_user(user_login,remember=rm)
            return redirect("/")
    return render_template("login.html")

@app.route("/profile")
@login_required
def profile():
    return render_template("profile.html")

@app.route("/logout")
@login_required
def logout():
    session.clear()
    return redirect("/")