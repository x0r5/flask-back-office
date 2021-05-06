from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email = email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
            else:
                flash('Incorrect password.', category='error')
        else:
            flash('User does not exists', category='error')
    data = request.form
    print(data)
    return render_template("login.html")

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        terms = request.form.get('terms')

        user = User.query.filter_by(email = email).first()
        if user:
            flash('User already exists with that email address!', category="error")
        elif len(email) < 4:
            flash('Email must be longer!', category='error')
        elif password1 != password2:
            flash('Your passwords do not match!', category='error')
        elif not terms:
            flash("You need to accept the terms and conditions!", category="error")
        else:
            new_user = User(email = email, name = name, password = generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created', category="success")
            login_user(user, remember=True)
            return redirect(url_for('views.home'))

    return render_template("sign_up.html")