# Importing the db instance from the current package
from . import db

# Importing UserMixin from Flask-Login for user model
from flask_login import UserMixin

# Importing func from SQLAlchemy for database functions
from sqlalchemy.sql import func

# Defining the User class inheriting from db.Model and UserMixin
class User(db.Model, UserMixin):
    # Defining database columns for the User model
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each user (primary key)
    email = db.Column(db.String(150), unique=True)  # Email column, max length of 150 characters, unique constraint
    password = db.Column(db.String(150))  # Password column, max length of 150 characters
    firstName = db.Column(db.String(150))  # First name column, max length of 150 characters

    