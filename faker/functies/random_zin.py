from random import choice, randint
from lijsten.nl_lorem import nl_woorden_lijst
from lijsten.us_lorem import us_word_list

def random_zin(lijst=None, taal="nl") -> str:
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
