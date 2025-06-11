from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = "supersecretkey"

@app.route("/")
def home():
    if "username" in session:
        return f"أهلاً وسهلاً بكم حياكم الله يا {session['username']}"
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == "admin" and password == "admin123@":
            session["username"] = username
            return redirect(url_for("home"))
        flash("بيانات الدخول غير صحيحة")
    return '''
        <form method="POST">
            اسم المستخدم: <input name="username"><br>
            كلمة المرور: <input name="password" type="password"><br>
            <input type="submit" value="تسجيل الدخول">
        </form>
    '''

@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("login"))