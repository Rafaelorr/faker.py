from random import choice
from lijsten.steden import steden

def random_stad() -> str:
    """
    Returns een random stad (onder andere uit de VS).

    Returns:
        stad (str)
    """
    return choice(steden)