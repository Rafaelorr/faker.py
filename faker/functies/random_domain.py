from random import choice
from faker.lijsten.domain_namen import domain_naam_lijst

def random_domain() -> str:
    domain_naam: str = choice(domain_naam_lijst)
    return domain_naam