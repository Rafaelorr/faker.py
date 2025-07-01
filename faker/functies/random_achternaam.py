from random import choice
from lijsten.achternamen import achternamen

def random_achternaam() -> str:
    """
    Returns een random achternaam.

    Returns: 
        Achternaam (str)
    """
    return choice(achternamen)
