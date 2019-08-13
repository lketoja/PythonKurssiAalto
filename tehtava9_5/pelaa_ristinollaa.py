# OPEY1 2017 /Y1 KESA 2019
# Testiohjelma tehtavaan 9.5
# Ohjelma, joka pelaa ristinollaa luokan kayttamalla luokkaa Ristinolla.
# Kirjoittanut Kerttu Pollari-Malmi

from ristinolla import *

# Funktio huolehtii pelin yhden vuoron pelaamisesta. Funktio saa 
# parametrina vuorossa olevaa pelaajaa kuvaavan vakion ja pelitilannetta 
# kuvaavan Ristinolla-olion.

def pelaa_vuoro(vuorossa, peli_menossa):
    print("Pelitilanne nyt:")
    print(peli_menossa)
    if vuorossa == Ristinolla.PELAAJA1:
        pelaajan_nimi = peli_menossa.kerro_pelaaja1()
    else:
        pelaajan_nimi = peli_menossa.kerro_pelaaja2()
    print("Vuorossa on {:s}.".format(pelaajan_nimi))
    vuoro_pelattu = False
    while not vuoro_pelattu:
        ruutu = input("Mihin ruutuun merkki lisataan?\n")
        osat = ruutu.split(":")
        try:
            x_koordi = int(osat[0])
            y_koordi = int(osat[1])
            if peli_menossa.lisaa_merkki(x_koordi, y_koordi, vuorossa):
                vuoro_pelattu = True
            else:
                print("Valitsemaasi ruutuun ei voi lisata merkkia.")
        except ValueError:
            print("Anna koordinaatit kokonaislukuina.")
        except IndexError:
            print("Koordinaatit pitaa antaa muodossa X:Y")


# Funktio kertoo kayttajalle pelin lopputuloksen. Funktio saa parametrina
# lopputulosta kuvaavan vakion seka pelia kuvaavan Ristinolla-olion.

def kerro_tulos(lopputulos, paattynyt_peli):
    print("Peli on paattynyt. Pelilaudan tilanne lopuksi:")
    print(paattynyt_peli)
    if lopputulos == Ristinolla.PELAAJA1:
        print("Voittaja on", paattynyt_peli.kerro_pelaaja1())
    elif lopputulos == Ristinolla.PELAAJA2:
        print("Voittaja on", paattynyt_peli.kerro_pelaaja2())
    else:
        print("Peli paattyi tasapeliin.")


def main():
    print("Tervetuloa pelaamaan ristinollaa {:d}x{:d}-ruudukolla.".format(\
          Ristinolla.KOKO, Ristinolla.KOKO))
    print("Ruutujen koordinaatit annetaan muodossa X:Y.")
    print("Koordinaatit alkavat vasemmasta alakulmasta nollasta.")
    eka_nimi = input("Kuka on ensimmainen pelaaja?\n")
    toka_nimi = input("Kuka on toinen pelaaja?\n")
    peli = Ristinolla(eka_nimi, toka_nimi)
  
    vuorossa = Ristinolla.PELAAJA1
    tulos = peli.peli_paattynyt()
    while tulos == Ristinolla.KESKEN:
        pelaa_vuoro(vuorossa, peli)
        if vuorossa == Ristinolla.PELAAJA1:
            vuorossa = Ristinolla.PELAAJA2
        else:
            vuorossa = Ristinolla.PELAAJA1
        tulos = peli.peli_paattynyt()
    kerro_tulos(tulos, peli)
    
    
main()