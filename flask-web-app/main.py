# Importing the create_app function from the website package
from website import create_app

# Creating the Flask application using the create_app function
app = create_app()

# Running the Flask application if the script is executed directly
if __name__ == '__main__':
    app.run(debug=True)  # Running the app in debug mode for development
