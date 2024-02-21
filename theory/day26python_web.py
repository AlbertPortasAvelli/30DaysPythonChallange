### Day 26: Python for Web ###

# 1. Introduction
# Python is a general-purpose programming language that can be used for web development. There are many Python web frameworks available, with Django and Flask being the most popular ones. Today, we'll explore how to use Flask for web development.

# 1.1 Flask
# Flask is a web development framework written in Python. It uses the Jinja2 template engine and can be integrated with other modern frontend libraries like React.

# 2. Virtual Environment Setup
# Before starting with Flask, it's recommended to set up a virtual environment to isolate project dependencies from the local machine dependencies.

# 3. Folder Structure
# After setting up the project, the folder structure should resemble the following:

# ├── Procfile
# ├── app.py
# ├── env
# │   ├── bin
# ├── requirements.txt
# ├── static
# │   └── css
# │       └── main.css
# └── templates
#     ├── about.html
#     ├── home.html
#     ├── layout.html
#     ├── post.html
#     └── result.html

# 4. Setting Up Project Directory
# Follow these steps to get started with Flask:

# 4.1 Step 1: Install virtualenv
# Run the following command to install virtualenv:
# pip install virtualenv

# 4.2 Step 2: Set up project directory
# Create a project directory and set up a virtual environment named 'venv':

# mkdir python_for_web
# cd python_for_web/
# virtualenv venv
# source venv/bin/activate

# Install Flask:
# pip install Flask

# Create a file named 'app.py' in the project directory and add the following code:

# 5. Creating Routes
# Define routes for different pages in the web application. Here's an example of creating the home and about routes:

# 5.1 Creating the Home Route
from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Welcome</h1>'

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

# 5.2 Creating the About Route
from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/about')
def about():
    return '<h1>About us</h1>'

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

# 6. Rendering HTML Templates
# Instead of returning plain text responses, Flask allows rendering HTML templates using the render_template function. Here's how to render HTML files for the home and about pages:

# 6.1 Rendering the Home Page
from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

# 6.2 Rendering the About Page
from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

# 7. Creating a Layout
# To avoid repetition of code in template files, create a layout and import it into every page. Here's an example of creating a layout named 'layout.html':

# 8. Serving Static Files
# Serve static files like CSS using the url_for module. Create a 'static' folder in the project directory and place CSS files inside it. Here's how to serve static files:

# 9. Deployment
# Deploy the Flask application using Heroku, a free hosting service. Follow these steps to deploy the application:

# 9.1 Creating Heroku Account
# Heroku provides a free deployment service for both frontend and fullstack applications. Create an account on Heroku and install the Heroku CLI for your machine.

# 9.2 Logging in to Heroku
# Run the following command to log in to Heroku using the CLI:

# heroku login

# 9.3 Create Requirements and Procfile
# Before pushing the code to the remote server, create a 'requirements.txt' file containing the project dependencies and a 'Procfile' specifying the command to run the application.

# 9.4 Pushing Project to Heroku
# Initialize a git repository, add files, commit changes, and push to Heroku master.

# 9.5 Open the Deployed Application
# After deployment, open the deployed application to see the result.

# Example project structure and code snippets have been provided to illustrate each step of the process.