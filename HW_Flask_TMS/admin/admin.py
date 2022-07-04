from flask import Blueprint, request, url_for, render_template, flash, session
from werkzeug.utils import redirect

admin = Blueprint('admin', __name__, template_folder='templates', static_folder='static')

navbar = [
    {"url": ".index", "title": "Admin panel"},
    {"url": ".sign_out", "title": "Sign out"}]

def login_admin():
    session["admin_logged"] = 1


def is_logged():
    return True if session.get("admin_logged") else False


def logout_admin():
    session.pop("admin_logged", None)


@admin.route("/")
def index():
    if not is_logged():
        return redirect(url_for(".login"))

    return render_template("admin/admin_dashboard.html", navbar=navbar, title="Admin panel")


@admin.route("/sign-in", methods=['GET', 'POST'])
def login():
    if is_logged():
        return redirect(url_for(".index"))

    if request.method == "POST":
        if request.form["user"] == "admin" and request.form["pswrd"] == "admin123":
            login_admin()
            return redirect(url_for(".index"))  # dot means that we taking index function from our Blueprint
            # instead of main (general) index function
        else:
            flash("Please, check your input data", category="warning")

    return render_template("admin/admin_sign_in.html", title="Admin panel")


@admin.route("/admin-sign-out", methods=['GET', 'POST'])
def sign_out():
    if is_logged():
        logout_admin()
        flash("Admin has been logged out!", category='info')
        return redirect(url_for('.login'))

    else:
        return redirect(url_for(".login"))

