from random import choice

def random_companyName() -> str:
    companyName_list: list[str] = ["Walmart","Amazon","Apple","UnitedHealth Group","Berkshire Hathaway","CVS Health","ExxonMobil","Alphabet",
                                  "McKesson Corporation","Cencora","Costco","JPMorgan Chase","Microsoft","Cardinal Health","Chevron Corporation",
                                  "Cigna","Ford Motor Company","Bank of America","General Motors","Elevance Health","Citigroup","Centene",
                                  "The Home Depot","Marathon Petroleum","Kroger","Philips 66","Fannie Mae","Walgreens Boots Alliance","Valero Energy",
                                  "Meta Platforms","Verizon Communications","AT&T","Comcast","Wells Fargo","Goldman Sachs","Freddie Mac","Target Corporation",
                                  "Humana","State Farm","Tesla","Morgan Stanley","Johnson & Johnson","Archer Daniels Midland","PepsiCo","United Parcel Service",
                                  "FedEx","The Walt Disney Company","Dell Technologies","Lowe's","Procter & Gamble","Energy Transfer Partners","Boeing",
                                  "Albertsons","Sysco","RTX Corporation","General Electric","Lockheed Martin","American Express","Caterpillar","MetLife","Cargill",
                                  "Koch Industries","Publix Super Markets","Mars, Incorporated","H-E-B","Reyes Holdings","Enterprise Holdings","C& S Wholesale Grocers",
                                  "Love's","Southern Glazer's Wine and Spirits","Nvidia"]
    companyName: str = choice(companyName_list)
    return companyName