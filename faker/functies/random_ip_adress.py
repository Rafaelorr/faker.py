from random import randint

def random_ip_adress(version="v4") -> str:
    """
    Geneert een random ip adress (standaard: ip v4).

    Args:
        version (string): v4 voor ip v4 en v6 voor ip v6
    
    Returns:
        ip_adress (str)
    """
    if version == "v4":
        return ".".join(str(randint(0, 255)) for _ in range(4))
    elif version == "v6":
        return ":".join("{:04x}".format(randint(0, 0xFFFF)) for _ in range(8))
    else:
        raise ValueError("Geen correct versie ingegeven.")