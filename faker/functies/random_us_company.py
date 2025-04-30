from random import choice
from faker.lijsten.us_companies import companyName_list

def random_companyName() -> str:
    companyName: str = choice(companyName_list)
    return companyName