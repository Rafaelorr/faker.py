from random import choice
from lijsten.top_level_domain_lijst import top_level_domain_lijst

def random_top_level_domain() -> str:
    """
    Returns een random tld (top level domain) uit de lijst van ICANN.

    Returns:
        tld (str)
    """
    return choice(top_level_domain_lijst)