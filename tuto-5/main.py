from flask import Flask, redirect, url_for, render_template, request, session
from datetime import timedelta
app = Flask(__name__)
app.secret_key = "root"
app.permanent_session_lifetime = timedelta(minutes=5)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        session["user"] = request.form["name"]
        return redirect(url_for("user", usr=user))
    else:
        if "user" in session:
            return redirect(url_for("user"))
        return render_template("login.html")


@app.route("/user")
def user():
    if "user" in session:
        usr = session["user"]
        return f"Hello {usr}"
    else:
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    if "user" in session:
        session.pop("user", None)

    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
