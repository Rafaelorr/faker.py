from random import randint

def random_nummer(min_num:float,max_num:float) -> float:
    """
    Geneert een random nummer.

    Args:
        min_num (float): het min nummer
        max_num (float): het max nummer
    
    Returns:
        num (float): het random nummer
    """
    num = randint(min_num,max_num)
    return num