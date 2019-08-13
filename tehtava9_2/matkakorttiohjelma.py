from matkakortti import *

def main():
    matkakortti1 = Matkakortti("Teemu Virtanen", 2)
    matkakortti1.lisaa_saldoa(25.00)
    matkakortti1.osta_lippu(1.50)
    print("Teemu osti matkakortillaan lipun, kortin saldo on nyt", matkakortti1.kerro_saldo(), "euroa.")
    
    toinen_nimi = input("Mika on toisen kortin omistajan nimi?")
    print("Mika on toisen kortin tyyppi (1 = Aikuinen, 2 = Lapsi)?")
    tyyppi = lue_kortin_tyyppi()
    matkakortti2 = Matkakortti(toinen_nimi, tyyppi)
    print("Paljonko lisataan toiselle kortille saldoa (eur)?")
    saldo = lue_desimaaliluku()
    matkakortti2.lisaa_saldoa(saldo)
    
    print("Korttien tiedot:")
    print(matkakortti1)
    print(matkakortti2)
    
    print("Muutetaan Teemun kortin tyyppi ja nollataan sen saldo.")
    matkakortti1.muuta_tyyppi(1)
    matkakortti1.nollaa_saldo()
    
    print("Minka hintainen lippu ostetaan toiselle kortille?")
    hinta = lue_desimaaliluku()
    if matkakortti2.osta_lippu(hinta):
        print("Lipun osto onnistui.")
    else:
        print("Lipun osto ei onnistunut.")
        
    print("Korttien tiedot muutosten jalkeen:")
    print(matkakortti1)
    print(matkakortti2)
    

def lue_kortin_tyyppi():
    tyyppi_onnistui = False
    while not tyyppi_onnistui:
        try:
            tyyppi = int(input()) #Huomaa, etta sinun pitaa itse ensin tulostaa paaohjelmassa kysymys 
            # "Mika on toisen kortin tyyppi (1 = Aikuinen, 2 = Lapsi)?" print-laskylla
            if tyyppi in (Matkakortti.AIKUINEN, Matkakortti.LAPSI):
                tyyppi_onnistui = True
            else:
                print("Kortin tyyppi on vaarin!")
                print("Anna uusi!")
        except ValueError:
            print("Kortin tyyppi on vaarin!")
            print("Anna uusi!")
    return tyyppi

def lue_desimaaliluku():
    luku_onnistui = False
    while not luku_onnistui:
        try:
            luku = float(input()) # huomaa, etta sinun pitaa ensin tulostaa paaohjelmassa sopiva kysymys print-kaskylla
            luku_onnistui = True
        except ValueError:
            print("Virheellinen desimaaliluku!")
            print("Anna uusi!")
    return luku

main()