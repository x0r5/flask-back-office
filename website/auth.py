from flask import Blueprint, render_template, request, flash

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
            flash('Your passwords do not match!', categor='error')
        else:
            flash('Account created', category="success")
    return render_template("sign_up.html")