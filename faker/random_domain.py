from random import choice

def random_domain() -> str:
    domain_naam_lijst: list[str] = ["gmail",
"yahoo",
"hotmail",
"yahoo.co",
"hotmail.co",
"outlook",]
    domain_naam: str = choice(domain_naam_lijst)
    return domain_naam