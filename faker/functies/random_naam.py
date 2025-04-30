from random import choice
from faker.lijsten.namen import namenlijst_alle_geslachten, mannelijke_namen, vrouwelijke_namen

def random_naam(geslacht:str) -> str:
    """
    Genereert een naam op basis van een geslacht

    Args:
        geslacht (string): Het geslacht (m) voor mannelijk en (f) voor vrouwelijk, als het anders is het de beide geslachten

    Returns:
        str: De gekozen naam
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