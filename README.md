# Flask Web Application with Authentication

A production-oriented Python web application built with **Flask**, focused on secure user authentication and database integration. This project demonstrates best practices for building scalable web applications using the Flask Application Factory pattern.

The application provides a solid foundation that can be extended into real-world systems such as dashboards, administrative platforms, or SaaS products.

---

## Overview
This project showcases practical backend web development skills, including authentication workflows, database modeling, and modular application design. It emphasizes clean architecture, maintainability, and security fundamentals.

---

## Learning Context

The initial project structure is partially based on a Flask tutorial and was developed as a
hands-on exercise to strengthen backend development skills.
The application was extended, refactored, and customized to demonstrate
authentication workflows, database integration, and scalable application design.

---

## Key Features

- User registration and authentication system
- Secure password hashing and credential storage
- Login and logout functionality
- User-specific data association
- Database integration using ORM
- Modular and scalable Flask architecture
- Application Factory pattern implementation

---

## Technologies & Tools

- Python
- Flask
- Flask-Login
- Flask-SQLAlchemy
- SQLite (development database)
- HTML, CSS, Jinja2
- Git / GitHub
---

## Project Structure

```text
project/
│
├── instance/
│   ├──database.db         # Database
│
├── website/
│   ├── __init__.py        # Application factory
│   ├── models.py          # Database models
│   ├── auth.py            # Authentication logic
│   ├── views.py           # Core application routes
│   ├── templates/         # Jinja2 templates
│   └── static/            # Static assets
│
├── main.py                # Application entry point
└── README.md
```
---
## How to Run the Application Locally

1. Clone the repository

  git clone https://github.com/your-username/your-repo-name.git
  cd your-repo-name

2. Create a virtual environment

  python -m venv venv
  source venv/bin/activate   # On Windows: venv\Scripts\activate

3. Install dependencies

  pip install flask flask-login flask-sqlalchemy

4. Run the application

  python main.py

5. Open your browser

  http://127.0.0.1:5000

---

## Entry Point (main.py)

from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)  # Debug mode for development only


The application uses the Flask Application Factory pattern, making it easier to scale, test, and maintain.

---

## Authentication Workflow

- Users can create an account
- Credentials are securely stored in the database
- Authenticated users can log in and log out
- User-specific data is linked to the logged-in accoun

---

## Development Notes

- debug=True should only be used in development
- Replace SQLite with PostgreSQL or MySQL for production
- Add environment variables for secret keys in production

---

## Potential Enhancements

- Email verification
- Password reset functionality
- Role-based access control (RBAC)
- API integration
- Deployment with Docker or cloud platforms

---

## License

This project is open-source and available for educational and personal use.
