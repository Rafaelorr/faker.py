from random import choice
from lijsten.username_lijst import username_lijst

def random_username() -> str:
    """
    Returns een random gebruikersnaam uit een lijst

    Returns:
        username (str)
    """
    return choice(username_lijst)
