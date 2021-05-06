from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "logout"

@auth.route('/sign-up', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        terms = request.form.get('terms')


        if len(email) < 4:
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
            return redirect(url_for('views.home'))

    return render_template("sign_up.html")