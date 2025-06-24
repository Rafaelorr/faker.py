from random import choice
from faker.lijsten.slogans import slogans

def random_slogan() -> str:
    """
    Returns de slogan van een random vs bedrijf.

    Returns:
        slogan (str)
    """
    return choice(slogans)