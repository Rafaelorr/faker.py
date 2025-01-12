from random import choice

def random_domain() -> str:
    domain_naam_lijst: list[str] = []
    domain_naam: str = choice(domain_naam_lijst)
    return domain_naam