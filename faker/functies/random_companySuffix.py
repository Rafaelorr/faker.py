from random import choice

def random_company_suffix() -> str:
    """
    Returns een random bedrijf suffix (bv. Corp).
    
    Returns:
        company suffix (str)
    """
    company_suffix_list: tuple[str] = (
    "Ltd",
    "Ltd.",
    "S.A.",
    "SA",
    "A.G.",
    "AG",
    "N.V.",
    "NV",
    "Ltee",
    "B.V.",
    "BV",
    "GmbH",
    "L.L.C.",
    "LLC",
    "SIA",
    "Sia",
    "Inc.",
    "Inc",
    "Corp.",
    "Corp",
    "Pte. Ltd"
    )
    company_suffix: str = choice(company_suffix_list)

    return company_suffix
