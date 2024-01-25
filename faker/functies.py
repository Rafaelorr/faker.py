from random import choice

def random_naam():
    with open('faker/namen.txt','r') as file:
        namen_lijst = file.read()
        list(namen_lijst)
        print(type(namen_lijst))
    return namen_lijst
print(random_naam())