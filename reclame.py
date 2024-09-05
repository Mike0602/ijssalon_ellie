from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):

    nieuwe_prijs = prijs * (1 - korting)
    
    resultaat = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {nieuwe_prijs:.2f} euro."

    return resultaat

print(aanbieding_1("aardbei", 4, 0.goo1))

def inkomsten_totaal(inkomsten, btw):
    totaal = sum(inkomsten)

    btw_bedrag = totaal * btw

    resultaat = f"Het totaal van alle inkomsten van deze week is {totaal:.2f} euro, waarover {btw_bedrag:.2f} euro btw betaald dient te worden."

    return resultaat

week_inkomsten = [220, 430, 125, 160, 205, 90, 345]
btw_percentage = 0.09
resultaat = inkomsten_totaal(week_inkomsten, btw_percentage)
print(resultaat)

def laag_en_hoog(mijn_lijst):
    
    laagste_waarde = min(mijn_lijst)
    hoogste_waarde = max(mijn_lijst)

    return [laagste_waarde, hoogste_waarde]

inkomsten = [220, 430, 125, 160, 205, 90, 345]
resultaat = laag_en_hoog(inkomsten)
print(resultaat)    

def gemiddelde(mijn_lijst):
    
    som = sum(mijn_lijst)
    aantal = len(mijn_lijst)
    gemiddelde_waarde = som / aantal
    
    return f"De gemiddelde inkomsten deze week zijn {gemiddelde_waarde:.2f} euro."

inkomsten = [220, 430, 125, 160, 205, 90, 345]
resultaat = gemiddelde(inkomsten)
print(resultaat)

def laag_en_hoog(mijn_lijst):
    laagste_waarde = min(mijn_lijst)
    hoogste_waarde = max(mijn_lijst)
    return [laagste_waarde, hoogste_waarde]

def meervoudig(invoer_lijst):

    resultaat = laag_en_hoog(invoer_lijst)
    
    return resultaat
lijst = [10, 5, 3, 2, 1, 2, 9]
print(meervoudig(lijst))

def laag_en_hoog(mijn_lijst):
    laagste_waarde = min(mijn_lijst)
    hoogste_waarde = max(mijn_lijst)
    return [laagste_waarde, hoogste_waarde]

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    
    resultaat = mijn_functie_2(korte_lijst)
    
    return resultaat
lijst = [10, 5, 3, 2, 1, 2, 9]
print(combinatie(lijst))  