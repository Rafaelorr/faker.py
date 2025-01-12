from random import choice

def random_companySuffix() -> str:
    companySuffix_list: list[str] = ["Ltd","Ltd.","S.A.","SA","A.G.","AG","N.V.","NV","Ltee","B.V.","BV","GmbH","L.L.C.","LLC","SIA","Sia","Inc.","Inc","Corp.","Corp","Pte. Ltd"]
    companySuffix: str = choice(companySuffix_list)
    return companySuffix