from random import choice
from faker.lijsten.slogans import slogans

def random_slogan() -> str:
    return choice(slogans)