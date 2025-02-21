from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# Extension that integrates SQLAlchemy with Flask.

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
#DeclarativeBase, Mapped, and mapped_column: Used to define database models using SQLAlchemy ORM.

from sqlalchemy import Integer, String, Float
#SQLAlchemy data types.

import os

# Initialize Flask app
app = Flask(__name__)



# Configure Database
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(basedir, 'new-book-collection.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Optional, suppresses warning
# basedir: Gets the absolute path of the current file’s directory.
# SQLALCHEMY_DATABASE_URI: Specifies the database location using SQLite.
# "sqlite:///": Prefix indicating an SQLite database, followed by the path to the .db file.
# SQLALCHEMY_TRACK_MODIFICATIONS = False: Disables tracking modifications to suppress a warning.



# Define Base Class
class Base(DeclarativeBase):
    pass
# DeclarativeBase is the base class for all SQLAlchemy models.
# This class is required because Flask-SQLAlchemy uses it to define the ORM structure.


# Initialize SQLAlchemy
db = SQLAlchemy(model_class=Base)
db.init_app(app)
# Creates an instance of SQLAlchemy with the Base class.
# db.init_app(app): Links the Flask app to the SQLAlchemy instance.

# Define Book Model
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
# inherits db.Model to define database model

    def __repr__(self):
        return f'<Book {self.title}>'
#__repr__: Special method that returns a string representation
# of the object (used for debugging). Here if we print book object it prints title of book
# instead of <obj...08...> Here, each object is like a each row of table which has
# attributes that represents each column-value of the table

# Create Tables
with app.app_context():
    db.create_all()

# app.app_context(): Provides the application context, which is needed when using SQLAlchemy outside of a request.
# db.create_all(): Creates the database and tables based on the models defined.

# Insert a Record
with app.app_context():
    new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
    db.session.add(new_book)
    db.session.commit()
    print("Book added successfully!")
