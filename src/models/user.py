from flask_sqlalchemy import SQLAlchemy
from db.db import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    role = db.Column(db.Text, nullable=False)

    characters = db.relationship('Character', backref='user', lazy=True)

    def __repr__(self):
        return f'<User {self.username}>'