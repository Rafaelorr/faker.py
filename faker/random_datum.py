import random
import time
    
def str_time_prop(start:str, end:str, time_format:str, prop:float):
    """
    Deze functie genereert een random datum tussen twee datums.
    Die twee datums moeten in een speficieke format zijn..
    Voorbeeld van dat format: 1/1/2008 1:30 PM

    Returns:
       string: de datum
    """
    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(time_format, time.localtime(ptime))


def random_date(start:str, end:str, prop:float):
    return str_time_prop(start, end, '%m/%d/%Y %I:%M %p', prop)
    
print(random_date("1/1/2008 1:30 PM", "1/1/2030 12:50 PM", random.random()))