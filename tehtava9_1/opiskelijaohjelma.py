# OPEY1 2017 / Y1 KESA 2019
# Testiohjelma tehtavassa 9.1 muutettavan Opiskelija-luokan
# testaamiseen.
# Kirjoittanut Kerttu Pollari-Malmi

import opiskelija

def lue_kokonaisluku():
    luku_onnistui = False
    while not luku_onnistui:
        try:
            luku = int(input())
            luku_onnistui = True
        except ValueError:
            print("Virheellinen kokonaisluku!")
            print("Anna uusi!")
    return luku

def main():
    nimi1 = input("Anna 1. opiskelijan nimi:\n")
    op_nro1 = input("Anna 1. opiskelijan opiskelijanumero:\n")
    kurssilainen1 = opiskelija.Opiskelija(nimi1, op_nro1)
    nimi2 = input("Anna 2. opiskelijan nimi:\n")
    op_nro2 = input("Anna 2. opiskelijan opiskelijanumero:\n")
    kurssilainen2 = opiskelija.Opiskelija(nimi2, op_nro2)

    print("Anna 1. opiskelijan tenttiarvosana.")
    tentti1 = lue_kokonaisluku()
    kurssilainen1.muuta_tenttiarvosana(tentti1)
    print("Anna 1. opiskelijan harjoitusarvosana.")
    harjoitus1 = lue_kokonaisluku()
    kurssilainen1.muuta_harjoitusarvosana(harjoitus1)

    print("Anna 2. opiskelijan tenttiarvosana.")
    tentti2 = lue_kokonaisluku()
    kurssilainen2.muuta_tenttiarvosana(tentti2)
    print("Anna 2. opiskelijan harjoitusarvosana.")
    harjoitus2 = lue_kokonaisluku()
    kurssilainen2.muuta_harjoitusarvosana(harjoitus2)

    print("1. opiskelijan tiedot:")
    print(kurssilainen1)
    print("Kurssiarvosana:", kurssilainen1.laske_kokonaisarvosana())

    print("2. opiskelijan tiedot:")
    print(kurssilainen2)
    print("Kurssiarvosana:", kurssilainen2.laske_kokonaisarvosana())
    
main()