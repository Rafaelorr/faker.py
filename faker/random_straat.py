from random import choice
from faker.lijsten.straten import us_straat_namen

def random_straat():
    return choice(us_straat_namen)