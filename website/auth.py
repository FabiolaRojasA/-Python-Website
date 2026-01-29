from flask import Blueprint, render_template, request, flash, redirect, url_for 
from flask_login import login_user, login_required, logout_user, current_user
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from email_validator import validate_email, EmailNotValidError


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login(): 
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
       
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True) 
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/signup', methods=['GET', 'POST'])
def signup(): 

    if request.method == 'POST':
        email = request.form.get('email')
        firstname = request.form.get('firstname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        # Here you would typically add logic to create a new user
       
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif not is_valid_email(email):
            flash('Please enter a valid email address.', category='error')
            pass
        elif len(firstname) < 2:
            flash('First Name must be greater than 1 characters.', category='error')
            pass
        elif password1 != password2:
            flash('Passwords do not match.', category='error')
            pass
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
            pass
        else:
            new_user = User(email=email, first_name=firstname, password=generate_password_hash(password1, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit() # Save the new user to the database
            login_user(new_user, remember=True) 
            flash('Account created!', category='success') 
            return redirect(url_for('views.home'))

    return render_template("signup.html", user=current_user)

def is_valid_email(email):
    try:
        # Validate.
        valid = validate_email(email)
        # Update with the normalized form.
        email = valid.email
        return True
    except EmailNotValidError as e:
        # Email not valid.
        return False