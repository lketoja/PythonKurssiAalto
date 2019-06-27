'''
Created on 20.6.2019

@author: Lotta Ketoja
'''
def main():
    print("Ohjelma laskee ja tulostaa tietoja joukkueen pyorailemista kilometreista.")
    nimilista = ["Sanna", "Vilma", "Joel", "Jimmy"]
    sanakirja = {"Sanna":[], "Vilma":[], "Joel":[], "Jimmy":[]}
    joukkueen_kilometrit = 0
    for nimi in nimilista:
        sanakirja[nimi] = lue_kilometrit(nimi)
    print("Nimi Kokonaiskilometrit Keskimaarin")
    for nimi in nimilista:
        summa = laske_kokonaiskilometrit(nimi, sanakirja)
        joukkueen_kilometrit += summa
        kilometrilistan_pituus = len(sanakirja[nimi])
        if kilometrilistan_pituus == 0:
            keskiarvo = 0
        else:
            keskiarvo = laske_keskimaaraiset_kilometrit(summa, kilometrilistan_pituus)
        print("{:7s}{:7d}{:16.2f}".format(nimi, summa, keskiarvo))
    print("Koko joukkueen kokonaiskilometrit:", joukkueen_kilometrit)    
    
def lue_kilometrit(nimi):
    syote = input("Anna henkilon " + nimi + " kilometrimaarat.\n")
    kilometrit = syote.split()
    for i in range(len(kilometrit)):
        kilometrit[i] = int(kilometrit[i])
    return kilometrit

def laske_kokonaiskilometrit(nimi, sanakirja):
    kilometrilista = sanakirja[nimi]
    return sum(kilometrilista)

def laske_keskimaaraiset_kilometrit(kokonaiskilometrit, paiva_lkm):
    return kokonaiskilometrit / paiva_lkm

main()
