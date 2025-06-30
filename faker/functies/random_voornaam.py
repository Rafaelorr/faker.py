from random import choice
from faker.lijsten.namen import mannelijke_namen, vrouwelijke_namen

def random_voornaam(geslacht:str) -> str:
    """
    Returns een voornaam op basis van het gegeven geslacht.

    Args:
        geslacht (string): m voor mannelijk en f voor vrouwelijk, iets anders voor unisex

    Returns:
        voornaam (str): de voornaam
    """
    namen_lijst:list[str] = []
    if geslacht == "m":
        namen_lijst.extend(mannelijke_namen)
    elif geslacht == "f":
        namen_lijst.extend(vrouwelijke_namen)
    else:
        namen_lijst.extend(mannelijke_namen)
        namen_lijst.extend(vrouwelijke_namen)
    return choice(namen_lijst)