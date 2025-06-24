from random import choice
from random_domain import random_domain
from random_top_level_domain import random_top_level_domain

def random_email() -> str:
    """
    Geneert een random email.

    Format: email_domain + random top level domain

    Returns:
        email (str)
    """
    email_domainen :tuple[str] = ("gmail","outlook","yahoo","mail.proton")
    domain :str = choice(email_domainen)
    tld :str = random_top_level_domain()
    email :str = domain + "." + tld
    return email