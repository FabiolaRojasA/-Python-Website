from . import db
from flask_login import UserMixin #import UserMixin for user session management
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True) # Unique identifier for each note
    data = db.Column(db.String(10000)) # Content of the note
    date = db.Column(db.DateTime(timezone=True), default=func.now()) # Date the note was created, defaults to current time
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # Foreign key linking to User

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True) # Unique identifier for each user
    email = db.Column(db.String(150), unique=True) # User's email address
    password = db.Column(db.String(150)) # Hashed password
    first_name = db.Column(db.String(150)) # User's first name
    notes = db.relationship('Note') # Relationship to Note model, allowing access to user's notes