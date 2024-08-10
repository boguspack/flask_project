![yang-shuo-uYHYGgvkz_Y-unsplash](https://github.com/user-attachments/assets/bf13af73-17cf-42c9-9b15-b647be0f9102)

# Flask Authentication Project

## Overview

This is a Flask web application that demonstrates user authentication using Flask-Login, form handling with Flask-WTF, and data management with Flask-SQLAlchemy. It provides a basic structure for building a Flask app with user login and registration functionality.

## Features

- User registration and login
- Session management
- Form validation
- SQLAlchemy ORM for database management

## Prerequisites

Ensure you have Python 3.8 or higher installed on your system. You also need `pip` to install the required Python packages.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/boguspack/flask_project.git
   cd your-repository
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install the Required Packages**

   ```bash
   pip install -r requirements.txt
   ```

5. **Set Up the Database**

   Make sure your database configuration is set up in `config.py`. You may need to run migrations if you're using Flask-Migrate:

   ```bash
   flask db upgrade
   ```

6. **Run the Application**

   ```bash
   flask run
   ```

   The application should be available at `http://127.0.0.1:5000/`.

## Usage

- **Register**: Go to `/register` to create a new user account.
- **Login**: Go to `/login` to sign in with your credentials.
- **Logout**: Click on the logout button to end your session.
- **Home**: Navigate to `/` to view the home page.

## Contributing

Feel free to fork the repository, make improvements, and create pull requests. Please make sure to follow the coding standards and include tests for new features or fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
