from random import choice
from lijsten.us_companies import companyName_list

def random_companyName() -> str:
    """
    Returns een random vs bedrijf.

    Returns:
        company_name (str)
    """
    company_name :str = choice(companyName_list)
    return company_name