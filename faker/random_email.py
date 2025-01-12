from random_domain import random_domain
from random_top_level_domain import random_top_level_domain

def random_email() -> str:
    domain: str = random_domain()
    tld: str = random_top_level_domain()
    email: str = domain + "." + tld
    return email