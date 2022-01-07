"""sqlalchemy/queries.py"""

from model import Human, Animal, connect_to_db, db
from flask import Flask

app = Flask(__name__)
connect_to_db(app)

# Get the human with the primary key 2
query_1 = None

# Get the first animal whose species is "fish"
query_2 = None

# Get all the animals with who belong to the human
# with primary key 5
query_3 = None

# Get all animals born in a year greater than (but not equal to) 2015.
query_4 = None

# Get all the humans with first names that start with "J"
query_5 = None

# Get all the animals who don't have a birth year
query_6 = None

# Get all the animals with species "fish" OR "rabbit"
query_7 = None

# Get all the humans who don't have an email address that
# contains "gmail"
query_8 = None

#
# Continue reading the instructions before you move on!
#


def print_humans_and_animals():
    """Print a directory of humans and their animals"""


def get_humans_by_animal_species(animal_species):
    """Return a list of Human objects who have animals of a certain species.

    The returned list doesn't have duplicates.

    Args:
        - animal_species: an animal's species.
    """