# Faker.py #

Een python package die sampel data geneert (volledig offline). <br>
Het is nog in development, dus er kunnen problemen zijn. <br>
Dus als er problemen zijn, kun je die melden in een issue (voeg een duidelijke beschrijving toe) of zelf fixen in een pull request. <br>

## Functies ##

**Naam**           | **functie**   |
--------           | -----------   |
**naam**           | Geneert een willekeurige naam. <br> Opties voor enkel mannelijke, vrouwelijke of alle namen.|
**us_adress**      | Geneert een willekeurig vs adress met een straat nummer, county naam en een staat. <br> Geeft het max straat nummer in als een int.|
**us_company**     | Kiest een random vs bedrijf uit een lijst van meer dan 7.000 bedrijven.|
**company suffix** | Kiest een random bedrijfachtervoegels zoals Corp of Inc.|
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

## Hoe maak je de package"

1. Download de source code `git clone https://github.com/Rafaelorr/faker.py.git`
2. Ga in de gedownloade folder `cd faker.py`
3. Edit pyproject.toml als je een nieuwe versie maakt
4. Maak de package `python3 -m build`

### Extras ###

Dit project was geinspireerd op [Faker.js](https://github.com/zuriby/Faker.js) door [zuriby](https://github.com/zuriby). <br>
Ik ben een python beginner, dus heb een beetje begrip als mijn code niet de beste is. <br>
