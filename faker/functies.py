from random import choice
from namen import namenlijst_alle_geslachten

def random_naam():
    namen_lijst = namenlijst_alle_geslachten
    return choice(namen_lijst)