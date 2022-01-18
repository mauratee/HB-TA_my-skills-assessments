"""sqlalchemy/queries.py"""

from model import Human, Animal, connect_to_db, db
from flask import Flask

app = Flask(__name__)
connect_to_db(app)

# Get the human with the primary key 2
query_1 = Human.query.get(2)

# Get the first animal whose species is "fish"
query_2 = Animal.query.filter_by(animal_species="fish").first()

# Get all the animals with who belong to the human
# with primary key 5
query_3 = Human.query.options(db.joinedload("animals")).get(5).animals

# Get all animals born in a year greater than (but not equal to) 2015.
query_4 = Animal.query.filter(Animal.birth_year > 2015).all()

# Get all the humans with first names that start with "J"
query_5 = Human.query.filter(Human.fname.like("J%")).all()

# Get all the animals who don't have a birth year
query_6 = Animal.query.filter(Animal.birth_year == None).all()

# Get all the animals with species "fish" OR "rabbit"
query_7 = Animal.query.filter(
    (Animal.animal_species == "fish") | (Animal.animal_species == "rabbit")
).all()

# Get all the humans who don't have an email address that
# contains "gmail"
query_8 = Human.query.filter(~(Human.email.contains("gmail"))).all()

# Continue reading the instructions before you move on!


def print_humans_and_animals():
    """Print a directory of humans and their animals"""
    for human in (
        Human.query.options(db.joinedload("animals")).order_by(Human.fname).all()
    ):
        print(f"{human.fname} {human.lname}")

        # lambda fxn is an anonymous function (similar to arrow fxn in JS)
        # that takes in parameter and function body to call on the parameter
        for animal in sorted(human.animals, key=lambda animal: animal.name):

            print(f"- {animal.name}, {animal.animal_species}")


def get_humans_by_animal_species(animal_species):
    """Return a list of Human objects who have animals of a certain species.

    The returned list doesn't have duplicates.

    Args:
        - animal_species: an animal's species.
    """

    humans = set()
    for animal in (
        Animal.query.options(db.joinedload("human"))
        .filter_by(animal_species=animal_species)
        .all()
    ):
        humans.add(animal.human)

    return list(humans)
