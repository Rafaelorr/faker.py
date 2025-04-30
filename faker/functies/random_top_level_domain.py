from random import choice
from faker.lijsten.top_level_domain_lijst import top_level_domain_lijst

def random_top_level_domain() -> str:
    return choice(top_level_domain_lijst)