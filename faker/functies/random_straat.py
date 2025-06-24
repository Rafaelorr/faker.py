from random import choice
from faker.lijsten.straten import us_straat_namen

def random_straat() -> str:
    """
    Returns een random us straat naam.

    Returns:
        us_straat (str)
    """
    return choice(us_straat_namen)