from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from freelance.models import db, User, Project
from freelance.forms import LoginForm, RegisterForm

main_bp = Blueprint("main_bp", __name__)

@main_bp.route("/")
def index():
    projects = Project.query.all()
    return render_template("index.html", projects=projects)

@main_bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for("main_bp.index"))
        flash("Invalid credentials", "danger")
    return render_template("login.html", form=form)

@main_bp.route("/signup", methods=["GET", "POST"])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Account created!", "success")
        return redirect(url_for("main_bp.login"))
    return render_template("signup.html", form=form)

@main_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main_bp.index"))
