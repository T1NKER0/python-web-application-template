# Importing necessary modules from Flask
from flask import Blueprint, render_template

# Importing login_required and current_user from Flask-Login
from flask_login import login_required, current_user

# Creating a Blueprint for the views
views = Blueprint('views', __name__)

# Route for the home page ('/')
@views.route('/')
@login_required  # Ensures that the user is logged in to access this route
def home():
    # Rendering the home template with the current user context
    return render_template("home.html", user=current_user)
