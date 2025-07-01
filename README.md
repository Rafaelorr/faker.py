**Dutch Version:**
# Faker.py #

Een python package die sampel data geneert (volledig offline). <br>
Het is nog in development, dus er kunnen problemen zijn. <br>
Dus als er problemen zijn, kun je die melden in een issue (voeg een duidelijke beschrijving toe) of zelf fixen in een pull request. <br>

## Functies ##

**Naam**           | **functie**   |
--------           | -----------   |
**voornaam**           | Geneert een willekeurige naam. <br> Opties voor enkel mannelijke, vrouwelijke of alle namen.|
**us_adress**      | Geneert een willekeurig vs adress met een straat nummer, county naam en een staat. <br> Geeft het max straat nummer in als een int.|
**us_company**     | Kiest een random vs bedrijf uit een lijst van meer dan 7.000 bedrijven.|
**companySuffix** | Kiest een random bedrijfachtervoegels zoals Corp of Inc.|
**datum**          | Geneert een random datum tussen twee datums. <br> Volgens dit format: Maand/Dag/Jaar PM of AM |
**domain**         | Kiest een random website uit lijst van meer dan 19.000 websites. <br> Deze bestaan uit tld en domain  |
**email**          | Geneert een random combinatie van 7 providers en een random tld.|
**slogan**         | Kiest een slogan uit een lijst van ongeveer 150 vs bedrijven.|
**stad**           | Kiest een random vs of uk stad.|
**straat**         | Kiest een random vs straatnaam.|
**tld**            | kiest een random tld uit de lijst van IACANN.|
**username**       | Geneert een random gebruikernaam.|
**nummer**         | Geneert een willekeurig nummer tussen de twee ingeven nummers <br> Opties voor ints en floats |
**achternaam**     | Geneert een willekeurige achternaam.|
**naam**           | Geneert een willekeurige naam (voornaam + achternaam).|
**ip_adress**        | Geneert een random ip adress. v4 voor een ip v4 adress en v6 voor een ip v6 adress.|

## Hoe maak je de package"

1. Download de source code `git clone https://github.com/Rafaelorr/faker.py.git`
2. Ga in de gedownloade folder `cd faker.py`
3. Edit pyproject.toml als je een nieuwe versie maakt
4. Maak de package `python3 -m build`

### Extras ###

Dit project was geinspireerd op [Faker.js](https://github.com/zuriby/Faker.js) door [zuriby](https://github.com/zuriby). <br>
Ik ben een python beginner, dus heb een beetje begrip als mijn code niet de beste is. <br>

**English Version:**
# Faker.py #

A python package that generates sample data (fully offline). <br>
It's still in development, so there might be problems. <br>
So if there are any problems, you can report them in an issue (add a clear description) or fix them yourself in a pull request. <br>

## Functions ##

**Name** | **function** |
-------- | ----------- |
**voornaam** | Generates a random name. <br> Options for only male, female or all names.|
**us_adress** | Generates a random vs address with a street number, county name and a state. <br> Gives the max street number as an int.|
**us_company** | Picks a random vs company from a list of over 7,000 companies.|
**companySuffix** | Picks a random company suffix such as Corp or Inc.|
**datum** | Generates a random date between two dates. <br> In this format: Month/Day/Year PM or AM |
**domain** | Chooses a random website from a list of over 19,000 websites. <br> These consist of tld and domain |
**email** | Generates a random combination of 7 providers and a random tld.|
**slogan** | Chooses a slogan from a list of about 150 vs companies.|
**stad** | Chooses a random vs or uk city.|
**straat** | Chooses a random vs street name.|
**tld** | Chooses a random tld from the IACANN list.|
**username** | Generates a random username.|
**nummer** | Generates a random number between the two entered numbers <br> Options for ints and floats |
**achternaam** | Generates a random last name.|
**naam**       | Generates a random name (first name + last name).|
**ip_adress**  | Generates a random ip adress. v4 for an ip v4 adress and v6 for an ip v6 adress.|

## How to make the package

1. Download the source code `git clone https://github.com/Rafaelorr/faker.py.git`
2. Go into the downloaded folder `cd faker.py`
3. Edit pyproject.toml if you are making a new version
4. Make the package `python3 -m build`

## Extras

This project was inspired by [Faker.js](https://github.com/zuriby/Faker.js) by [zuriby](https://github.com/zuriby). <br>
I am a python beginner, so please understand if my code is not the best. <br>