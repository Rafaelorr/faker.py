from functies.random_achternaam import random_achternaam
from functies.random_voornaam import random_voornaam

def random_naam(geslacht:str) -> str:
    """
    Returns een naam op basis van het gegeven geslacht.

    Args:
        geslacht (string): m voor mannelijk en f voor vrouwelijk, iets anders voor unisex
    
    Returns:
        naam (str): format = "{voornaam} {achternaam}"
    """
    if geslacht == "m":
        return f'{random_voornaam("m")} {random_achternaam()}'
    elif geslacht == "f":
        return f'{random_voornaam("f")} {random_achternaam()}'
    else:
        return f'{random_voornaam("a")} {random_achternaam()}'