from random import choice
from us_companies import companyName_list

def random_companyName() -> str:
    companyName: str = choice(companyName_list)
    return companyName