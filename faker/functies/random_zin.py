from random import choice, randint
from lijsten.nl_lorem import nl_woorden_lijst
from lijsten.us_lorem import us_word_list

def random_zin(lijst=None, taal="nl") -> str:
    """
    Genereert een willekeurige 'zin' bestaande uit een standaardwoordenlijst op basis van de gekozen taal.

    Parameters:
        lijst (list, optional): Een lijst met woorden om uit te kiezen. 
                                Als None, wordt een standaardlijst gebruikt op basis van 'taal'.
        taal (str, optional): De taal van de standaardwoordenlijst ('nl' voor Nederlands of 'us' voor Engels).
                              Standaard is 'nl'.

    Returns:
        str: Een string die een willekeurige 'zin' voorstelt (aaneengeschreven woorden, eindigend op een punt).

    Raises:
        ValueError: Als een onbekende taal is opgegeven en geen aangepaste lijst is meegegeven.
    """
    if lijst is None:
        if taal.lower() == "nl":
            lijst = nl_woorden_lijst
        elif taal.lower() == "us":
            lijst = us_word_list
        else:
            raise ValueError("Invalid language entered")

    zinwoorden = [choice(lijst) for _ in range(randint(1, len(lijst)))]
    zin = ''.join(zinwoorden) + '.'
    return zin
