# Y1 KESA 2019
# Ohjelma, joka pelaa laivanupotus luokan kayttamalla luokkaa laivanupotus.
# Kirjoittanut Ville Piiparinen
# Muokannut Joel Lahenius 2019

from laivanupotus import Laivanupotus

# Funktio huolehtii pelin yhden vuoron pelaamisesta. Funktio saa 
# parametrina vuorossa olevaa kenttaa kuvaavan Laivanupotus-olion.

def pelaa_vuoro(vuorossa):
    print("Seuraavan pelaajan ruudukko talla hetkella:")
    print(vuorossa)
    print("Vuorossa on pelaaja", vuorossa.kerro_pelaaja())
    vuoro_pelattu = False
    while not vuoro_pelattu:
        try:
            ruutu = int(input("Mihin ruutuun ammutaan?\n"))
            ampuminen = vuorossa.ammu(ruutu)
            if ampuminen == Laivanupotus.OSUMA:
                print("Osuma!")
                vuoro_pelattu = True
            elif ampuminen == Laivanupotus.OHI:
                print("Ohi!")
                vuoro_pelattu = True
            elif ampuminen == Laivanupotus.ULKONA:
                print("Antamaasi ruutuun ei voi ampua.")
            else:
                print("[Luokkasi palautti vaaran arvon]")
        except ValueError:
            print("Laivan sijainnin pitaa olla kokonaisluku.")
            


class LaivaError(Exception):
    """Luokka, joka kuvaa virheellisesta laivasta syntyvaa poikkeusta"""

# Apufunktio joka tutkii onko laiva oikean pituinen, yhtenainen ja vaaka- tai pystysuuntainen.
# Funktio palauttaa listan, joka sisaltaa laivan koordinaatit kokonaislukuina.
# Tai virhetapauksessa nostaa LaivaError-virheen
def tarkista_ja_muuta_koordinaateiksi(laiva_merkkijonona):
    try:
        koordinaatit = [int(x) for x in laiva_merkkijonona.strip().split(" ")]
    except ValueError:
        raise LaivaError("Laivojen koordinaattien tulee olla kokonaislukuja!")
    pituus = len(koordinaatit)
    if not 2 <= pituus <= 5:
        raise LaivaError("Laivan tulee olla 2-5 merkkia pitka!")
    for koord in koordinaatit:
        if not 1 <= koord <= 100:
            raise LaivaError("Kaikkien koordinaattien tulee olla valilta 1-100!")
    diff = koordinaatit[-1] - koordinaatit[-2]
    if diff not in (1, 10, -1, -10):
        raise LaivaError("Laivan tulee olla pysty- tai vaakasuorassa!")
    for i in range(pituus-1, 0, -1):
        if koordinaatit[i] - koordinaatit[i-1] != diff:
            raise LaivaError("Laivan tulee olla pysty- tai vaakasuorassa!")
        if sorted([koordinaatit[i] % 10, koordinaatit[i-1] % 10]) == [0,1]:
            raise LaivaError("Laivan tulee olla yhtenainen!")

    return koordinaatit
    
# Funktio tarkistaa, onko listoissa samoja arvoja
def leikkaavat(lst1, lst2):
    for item in lst1:
        if item in lst2:
            return True
    return False

# Funktio kysyy ja palauttaa laivojen koordinaatit yhdessa listassa
def pyyda_laivat():
    laiva_annettu = False
    while not laiva_annettu:
        laivat = []
        print("Anna 2-5 merkin pituisia laivoja pilkulla eroteltuna, laivaruudut valilyonnilla eroteltuna.")
        print("Esimerkiksi: 13 23, 54 64 74 84 94, 25 26 27")
        tiedot = input().split(",")
        try:
            for i in range(len(tiedot)):
                laiva = tarkista_ja_muuta_koordinaateiksi(tiedot[i])
                if not leikkaavat(laiva, laivat):
                    laivat += laiva
                else:
                    raise LaivaError("Laivat eivat saa olla paallekkain!")
        except LaivaError as e:
            print(e)
        else:
            laiva_annettu = True
    
    return laivat
    
def main():
    print("Laivanupotusta! Ruutujen koordinaatit ovat 1-100 alkaen")
    print("vasemmasta ylakulmasta, kasvaen aina vasemmalta oikealle.")
     
    eka_nimi = input("Anna ensin ensimmaisen pelaajan nimi.\n")
    print("Sijoita laivat. Toinen pelaaja katsoo muualle!")
    laivat1 = pyyda_laivat()
    
    toka_nimi = input("Anna toisen pelaajan nimi.\n")
    print("Sijoita laivat. Ensimmainen pelaaja katsoo muualle!")
    laivat2 = pyyda_laivat()
        
    peli1 = Laivanupotus(eka_nimi, laivat2)
    peli2 = Laivanupotus(toka_nimi, laivat1)
    
    vuorossa = peli1
    paattynyt = False
    while not paattynyt:
        pelaa_vuoro(vuorossa)
        paattynyt = vuorossa.peli_paattynyt()
        vuorossa = peli1 if vuorossa == peli2 else peli2
            
    if vuorossa == peli1:
        voittajan_nimi = peli2.kerro_pelaaja()
    else:
        voittajan_nimi = peli1.kerro_pelaaja()
    print("Peli ohi! Pelin voitti {:s}!".format(voittajan_nimi))

main()