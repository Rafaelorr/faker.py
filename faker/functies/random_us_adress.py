from random import randint, choice
from lijsten.us_counties import us_counties
from lijsten.us_staten import us_staten

def random_adress(max_adress:int) -> str:
    """
    Returns een vs adress.

    Format: adress + county + ", " + staat

    Args:
        max_adress (int): het hoogste getal dat mogelijk is als adress
    
    Returns:
        adress (str) 
    """
    adress_nummer:int = randint(1,max_adress)
    us_county :str = choice(us_counties)
    us_staat :str = choice(us_staten)

    adress = str(adress_nummer) + us_county + ", " + us_staat

    return adress