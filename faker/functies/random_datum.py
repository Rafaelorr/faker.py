import time
    
def str_time_prop(start:str, end:str, time_format:str, prop:float) -> str:
    stime :float = time.mktime(time.strptime(start, time_format))
    etime :float = time.mktime(time.strptime(end, time_format))

    ptime :float = stime + prop * (etime - stime)

    return time.strftime(time_format, time.localtime(ptime))

def random_date(start:str, end:str, prop:float) -> str:
    """
    Deze functie genereert een random datum tussen twee datums.

    Die twee datums moeten in een speficieke format zijn.

    VB: 1/1/2008 1:30 PM

    Args:
        start (str): begin datum
        end (str): eind datum

    Returns:
       datum (str): de genereerde datum
    """
    return str_time_prop(start, end, '%m/%d/%Y %I:%M %p', prop)
