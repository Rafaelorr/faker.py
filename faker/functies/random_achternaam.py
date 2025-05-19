from random import choice
from faker.lijsten.achternamen import achternamen

def random_achternaam() -> str:
    return choice(achternamen)
