from random import choice

def random_companySuffix():
    companySuffix_list = ["Ltd","Ltd.","S.A.","SA","A.G.","AG","N.V.","NV","Ltee","B.V.","BV","GmbH","L.L.C.","LLC","SIA","Sia","Inc.","Inc","Corp.","Corp","Pte. Ltd"]
    companySuffix = choice(companySuffix_list)
    return companySuffix