# Web Application Template

This web application template is built using Flask, a lightweight and flexible web framework for Python. It incorporates various web and database technologies to create a dynamic and interactive web experience.

## Description:

The web application allows users to perform various actions, such as logging in, signing up, and accessing different parts of the application based on their authentication status. It utilizes AJAX requests for asynchronous communication between the client and server, enhancing the user experience by updating parts of the web page without requiring full page reloads.

## Technologies Used:

- Flask: A Python web framework for building web applications.
- Jinja2: A templating engine for generating dynamic HTML content.
- Bootstrap: A front-end framework for designing responsive and mobile-first websites.
- jQuery: A JavaScript library for simplifying client-side scripting and DOM manipulation.
- SQLite: A lightweight relational database management system used for storing application data.
- SQLAlchemy: An ORM library for interacting with databases in Python.
- Flask-SQLAlchemy: A Flask extension for integrating SQLAlchemy with Flask applications.
- Flask-Login: A Flask extension for managing user authentication and sessions.

## Files Description:

- `app.py`: The main Python script containing the Flask application and its routes.
- `models.py`: Defines database models using SQLAlchemy for creating and managing database tables.
- `views.py`: Contains view functions for handling web requests and rendering HTML templates.
- `auth.py`: Handles user authentication-related routes and functions.
- `templates/`: Directory containing HTML templates for rendering web pages.
- `static/`: Directory containing static assets such as CSS, JavaScript, and image files.


