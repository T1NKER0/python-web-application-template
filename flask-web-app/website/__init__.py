# Importing necessary modules from Flask, SQLAlchemy, os, and Flask-Login
from flask import Flask  # Flask web framework
from flask_sqlalchemy import SQLAlchemy  # SQLAlchemy for ORM (Object Relational Mapping)
from os import path  # os.path module for file path operations
from flask_login import LoginManager  # Flask-Login for user session management

# Initializing SQLAlchemy instance
db = SQLAlchemy()

# Defining the database file name
DB_NAME = "database.db"

# Function to create and configure the Flask application
def create_app():
    # Initializing the Flask app
    app = Flask(__name__)
    
    # Setting the secret key for session management
    app.config['SECRET_KEY'] = 'qwerty'
    
    # Configuring the database URI for SQLAlchemy
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    
    # Initializing the SQLAlchemy instance with the app
    db.init_app(app)

    # Importing blueprints for modular structure
    from .views import views  # Importing views blueprint
    from .auth import auth  # Importing auth blueprint

    # Registering blueprints with URL prefixes
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # Importing the User model
    from .models import User

    # Function to create the database if it doesn't exist
    create_database(app)

    # Initializing the LoginManager
    login_manager = LoginManager()
    
    # Setting the default login view
    login_manager.login_view = 'auth.login'
    
    # Initializing the LoginManager with the app
    login_manager.init_app(app)

    # User loader function for Flask-Login
    @login_manager.user_loader
    def load_user(id):
        # Loading the user by ID
        return User.query.get(int(id))

    # Returning the configured app instance
    return app

# Function to create the database if it doesn't exist
def create_database(app):
    # Checking if the database file exists in the specified path
    if not path.exists('website/' + DB_NAME):
        # Creating the database within the app context
        with app.app_context():
            db.create_all()  # Creating all database tables
            print('Created Database!')  # Printing confirmation message
