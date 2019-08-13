
def main():
    tiedoston_nimi = input("Mista tiedostosta opiskelijoiden tiedot luetaan?\n")
    try:
        tiedosto = open(tiedoston_nimi, 'r')
        tilasto = {}
        laskuri = 0
        for rivi in tiedosto:
            rivi = rivi.rstrip()
            lista = rivi.split(',')
            if len(lista) != 4:
                print("Tiedostossa virheellinen rivi:", rivi)
                continue
            laskuri += 1 
            if lista[3] in tilasto:
                tilasto[lista[3]] += 1
            else:
                tilasto[lista[3]] = 1
        maalista = sorted(tilasto)
        print("Opiskelijoiden lukumaara kotimaittain")
        for maa in maalista:
            print("{:15s}{:3d}".format(maa, tilasto[maa]))
        print("-----------------------------------------")
        print("Yhteensa", laskuri, "opiskelijaa")
    except OSError:
        print("Virhe tiedoston lukemisessa. Ohjelma paattyy.")
main()