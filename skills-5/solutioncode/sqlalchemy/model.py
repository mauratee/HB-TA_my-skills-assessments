"""
Skills 5: SQLAlchemy

Part 1: Define Model Classes
"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Human(db.Model):
    """Data model for a human."""

    __tablename__ = "humans"

    human_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fname = db.Column(db.String(25), nullable=False)
    lname = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(100), nullable=False)

    animals = db.relationship("Animal", back_populates="human")

    def __repr__(self):
        return f"<Human human_id={self.human_id} fname={self.fname}>"


class Animal(db.Model):
    """Data model for an animal."""

    __tablename__ = "animals"

    animal_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    animal_species = db.Column(db.String(25), nullable=False)
    birth_year = db.Column(db.Integer)

    human_id = db.Column(db.Integer, db.ForeignKey("humans.human_id"))

    human = db.relationship("Human", back_populates="animals")

    def __repr__(self):
        return f"<Animal animal_id={self.animal_id} name={self.name} animal_species={self.animal_species}>"

def connect_to_db(app):
    """Connect the database to our Flask app."""

    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///animals"
    app.config["SQLALCHEMY_ECHO"] = False
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    print("Connected to db!")


if __name__ == "__main__":
    from flask import Flask

    app = Flask(__name__)
    connect_to_db(app)