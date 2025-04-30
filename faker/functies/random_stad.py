from random import choice
from faker.lijsten.steden import steden

def random_stad() -> str:
    return choice(steden)