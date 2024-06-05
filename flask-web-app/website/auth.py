# Importing necessary modules from Flask and other dependencies
from flask import Blueprint, render_template, request, flash, redirect, url_for  # Flask modules
from .models import User  # Importing the User model from the current package
from werkzeug.security import generate_password_hash, check_password_hash  # Security functions for hashing passwords
from . import db  # Importing the db instance from the current package (__init__.py)
from flask_login import login_user, login_required, logout_user, current_user  # Flask-Login functions

# Creating a Blueprint for authentication routes
auth = Blueprint('auth', __name__)

# Route for login with GET and POST methods
@auth.route('/login', methods=['GET', 'POST'])
def login():
    # Checking if the request method is POST
    if request.method == 'POST':
        # Retrieving email and password from the form
        email = request.form.get('email')
        password = request.form.get('password')

        # Querying the database for a user with the provided email
        user = User.query.filter_by(email=email).first()
        
        # If user exists in the database
        if user:
            # Checking if the provided password matches the stored hashed password
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')  # Flash success message
                login_user(user, remember=True)  # Logging in the user
                return redirect(url_for('views.home'))  # Redirecting to home page
            else:
                flash('Incorrect password, try again.', category='error')  # Flash error message for incorrect password
        else:
            flash('Email does not exist.', category='error')  # Flash error message for non-existent email

    # Rendering the login template with the current user context
    return render_template("login.html", user=current_user)

# Route for logout (requires user to be logged in)
@auth.route('/logout')
@login_required  # Ensures that the user is logged in to access this route
def logout():
    logout_user()  # Logging out the user
    return redirect(url_for('auth.login'))  # Redirecting to the login page

# Route for sign-up with GET and POST methods
@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    # Checking if the request method is POST
    if request.method == 'POST':
        # Retrieving form data
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        # Querying the database for a user with the provided email
        user = User.query.filter_by(email=email).first()
        
        # Validating the form data
        if user:
            flash('Email already exists.', category='error')  # Flash error message for existing email
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')  # Flash error message for short email
        elif len(firstName) < 2:
            flash('First name must be greater than 1 character.', category='error')  # Flash error message for short first name
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')  # Flash error message for password mismatch
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')  # Flash error message for short password
        else:
            # Creating a new user with the provided data
            new_user = User(
                email=email, 
                firstName=firstName, 
                password=generate_password_hash(password1, method='scrypt')  # Hashing the password
            )
            db.session.add(new_user)  # Adding the new user to the database session
            db.session.commit()  # Committing the session to save the new user to the database
            login_user(new_user, remember=True)  # Logging in the new user
            flash('Account created!', category='success')  # Flash success message
            return redirect(url_for('views.home'))  # Redirecting to home page

    # Rendering the sign-up template with the current user context
    return render_template("sign_up.html", user=current_user)
