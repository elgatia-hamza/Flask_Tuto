from flask import Blueprint, render_template

second = Blueprint("second", __name__, static_folder="static/",
                   template_folder="templates")


@second.route("/")
@second.route("/home")
def home():
    return render_template("admin.html")


@second.route("test/")
def test():
    return "<h1>Hello Admin!</h1>"
