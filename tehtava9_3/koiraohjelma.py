# Y1 KESA 2019
# Koiraohjelma kayttaa tehtavassa 9.3 luotavaa luokkaa Koira.
# Kirjoittanut Vilma Kahri ja Joel Lahenius

from koira import *

def input_number(viesti, minimi, maksimi, convert = int):
    while True:
        try:
            i = convert(input(viesti))
            if not minimi <= i <= maksimi:
                tyyppi = "kokonaisluku" if convert == int else "desimaaliluku"
                print("Luvun pitaa olla {:s} valilta {:d}-{:d}".format(tyyppi, minimi, maksimi))
                raise ValueError
            return i
        except ValueError:
            pass

def poistu(koira):
    return True
    
def kysy_valinta(koira):
    print("Mita {:s} haluaa tehda?".format(koira.kerro_nimi()))
    print("1 - Juokse")
    print("2 - Leiki")
    print("3 - Syo")
    print("4 - Nuku")
    print("5 - Tee temppu")
    print("(6 - Poistu ohjelmasta)")
    valinta = input_number("Valinta:\n", 1, 6)
    return valinta

VAIHTOEHDOT1 = ["-","vahan", "jonkin verran", "paljon", "tosi paljon"]
VAIHTOEHDOT2 = ["-","vahan aikaa", "jonkin aikaa", "kauan", "tosi kauan"]

def maaran_valinta_1():
    print("1 - Vahan")
    print("2 - Jonkin verran")
    print("3 - Paljon")
    print("4 - Tosi paljon")
    valinta = input_number("Valinta:\n", 1, 4, int)
    return valinta

def maaran_valinta_2():
    print("1 - Vahan aikaa")
    print("2 - Jonkin aikaa")
    print("3 - Kauan")
    print("4 - Tosi kauan")
    valinta = input_number("Valinta:\n", 1, 4, int)
    return valinta

def juoksu(koira):
    print("Kauanko {:s}n kanssa juostaan?".format(koira.kerro_nimi()))
    matka = maaran_valinta_2()
    matka_todellinen = koira.juokse(matka)
    if matka_todellinen > 0:
        print("{:s} jaksoi juosta {:s}.".format(koira.kerro_nimi(), VAIHTOEHDOT2[matka_todellinen]))
    else:
        print("{:s} ei jaksa juosta.".format(koira.kerro_nimi()))
    
def nukkuminen(koira):
    print("Kauanko {:s} haluaa nukkua?".format(koira.kerro_nimi()))
    aika = maaran_valinta_2()
    aika_todellinen =  koira.nuku(aika)
    if aika_todellinen > 0:
        print("{:s} nukkui {:s}.".format(koira.kerro_nimi(), VAIHTOEHDOT2[aika_todellinen]))
    else:
        print("{:s} ei ole vasynyt juuri nyt.".format(koira.kerro_nimi()))
        
def syominen(koira):
    print("Paljonko {:s}lle annetaan ruokaa?".format(koira.kerro_nimi()))
    ruokamaara = maaran_valinta_1()
    ruokamaara_todellinen = koira.syo(ruokamaara)
    if ruokamaara_todellinen > 0:
        print("{:s} jaksoi syoda {:s}.".format(koira.kerro_nimi(), VAIHTOEHDOT1[ruokamaara_todellinen]))
    else:
        print("{:s}lla ei ole nalka.".format(koira.kerro_nimi()))
    
def leikki(koira):
    print("Kauanko {:s}n kanssa leikitaan?".format(koira.kerro_nimi()))
    leikin_pituus = maaran_valinta_2()
    leikin_pituus_todellinen = koira.leiki(leikin_pituus)
    if leikin_pituus_todellinen>0:
        print("{:s} leikki iloisesti {:s}."
              .format(koira.kerro_nimi(), VAIHTOEHDOT2[leikin_pituus_todellinen]))
    else:
        print("{:s} on liian nalkainen leikkimiseen juuri nyt.".format(koira.kerro_nimi()))

def temppu(koira):
    print("Kuinka vaikeaa temppua yritetaan?")
    tempun_vaikeusaste = input_number("1 - Tosi helppo\n2 - Helppo\n3 - Keskivaikea\n4 - Vaikea\n5 - Tosi vaikea\nValinta:\n", 1, 5, int)
    onnistuiko = koira.tee_temppu(tempun_vaikeusaste)
    if onnistuiko:
        print("{:s} onnistui tempussa!".format(koira.kerro_nimi()))
    else:
        print("{:s}n taidot eivat ihan riittaneet talla kertaa.\nKokeile vaikka vahan helpompaa temppua.".format(koira.kerro_nimi()))

VALINTAFUNKTIOT =  {1: juoksu,
                    2: leikki,
                    3: syominen,
                    4: nukkuminen,
                    5: temppu,
                    6: poistu}
def main():
    print("Tervetuloa koiraohjelmaan")
    oma_nimi =  input("Anna nimi koirallesi:\n")
    oma_koira = Koira(oma_nimi)
    while True:
        print()
        print("--------------------------------")
        print(oma_koira)
        print("--------------------------------")
        valinta = kysy_valinta(oma_koira)
        if VALINTAFUNKTIOT[valinta](oma_koira):
            break
    print("Kiva, kun pidit hyvaa huolta {:s}-koirastasi! Nyt ohjelma paattyy.".format(oma_koira.kerro_nimi()))

main()