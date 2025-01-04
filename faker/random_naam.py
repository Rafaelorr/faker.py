from random import choice
from namen import namenlijst_alle_geslachten, mannelijke_namen, vrouwelijke_namen

def random_naam(geslacht:str) -> str:
    """
    Genereert een naam op basis van een geslacht

    Args:
        geslacht (string): Het geslacht (m) voor mannelijk en (f) voor vrouwelijk, als het anders is het de beide geslachten

    Returns:
        str: De gekozen naam
    """
    if geslacht == "m":
        namen_lijst:list = mannelijke_namen
    elif geslacht == "f":
        namen_lijst:list = vrouwelijke_namen
    else:
        namen_lijst:list = namenlijst_alle_geslachten
    return choice(namen_lijst)