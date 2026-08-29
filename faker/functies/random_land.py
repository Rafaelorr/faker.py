from random import choice
from lijsten.landen import landen

def random_land() -> str:
    """
    Returns de naam van een random land
    
    Returns:
        naam van een land (str)
    """

    return choice(landen)
