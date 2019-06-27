'''
Created on 26.6.2019

@author: Lotta Ketoja
'''
def main():
    tiedoston_nimi = input("Minka nimisesta tiedostosta lahtotiedot luetaan?\n")
    try:
        tiedosto = open(tiedoston_nimi, "r")
        yhteishinta = 0
        print("Lahetyksen arvo  alv (eur)  tulli (eur)  uusi hinta (eur)")
        for rivi in tiedosto:
            luku = rivi.rstrip()
            lahetyksen_arvo = float(luku)
            tulli = 0
            if lahetyksen_arvo < 0:
                alv = 0
            else:
                alv = 0.24 * lahetyksen_arvo
                if lahetyksen_arvo > 150:                
                    tulli = 0.047 * lahetyksen_arvo
            uusi_hinta = lahetyksen_arvo + alv + tulli
            yhteishinta += uusi_hinta
            print("{:15.2f}{:10.2f}{:12.2f}{:17.2f}".format(lahetyksen_arvo, alv, tulli, uusi_hinta))    
        print("Tuotteiden yhteissumma alv- ja tullimaksujen jalkeen {:.2f} euroa.".format(yhteishinta)) 
        
    except OSError:
        print("Tiedoston", tiedoston_nimi, "lukemisessa tuli virhe. Ohjelma paattyy.")
    except ValueError:
        print("Tiedostossa on virheellinen luku. Ohjelma paattyy.")
        
main()