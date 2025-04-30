from random import choice
from faker.lijsten.username_lijst import username_lijst

def random_Username() -> str:
    return choice(username_lijst)