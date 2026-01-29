from datetime import timedelta
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'ls ad ase fr tf' # Replace with a secure key (environment variables) in production, security sensitive, like sesion data
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' # SQLite database URI
   
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)  # Sesión expira en 30 min
    app.config['SESSION_COOKIE_SECURE'] = False  # True en producción con HTTPS
    app.config['SESSION_COOKIE_HTTPONLY'] = True  # No accesible desde JS
    app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'  # Protege de CSRF
    
   
    db.init_app(app)

    from .views import views
    from .auth import auth
    from .models import User

    app.register_blueprint(views, url_prefix='/') # Register views blueprint with URL prefix '/'
    app.register_blueprint(auth, url_prefix='/')

    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login' # Redirect to 'auth.login' for @login_required
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app
