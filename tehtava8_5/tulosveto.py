def main():
    tiedoston_nimi = input("Anna tulosvetotiedot sisaltavan tiedoston nimi.\n")
    try:
        tiedosto = open(tiedoston_nimi, 'r')
    except OSError:
        print("Tiedoston", tiedoston_nimi, "lukeminen ei onnistu. Ohjelma paattyy.")
        return
    
    vetokertoimet = {}
    laskuri = 0
    for rivi in tiedosto:
        laskuri += 1
        rivi = rivi.rstrip()
        lista = rivi.split(";")
        if len(lista) != 2:
            print("Virhe tiedostossa rivilla " + str(laskuri) + ".")
            continue
        try:
            kerroin = float(lista[1])
        except:
            print("Rivilla", laskuri, "on virheellinen luku.")
        vetokertoimet[lista[0]] = lista[1]
    
    while True:
        ottelu = input("Anna tulosveto muodossa: TPS-JYP:1-0\n")
        try:          
            rahasumma = float(input("Anna rahasumma euroina.\n"))
            if ottelu in vetokertoimet:
                kerroin = float(vetokertoimet[ottelu])
                voittosumma = kerroin * rahasumma
                print("Kyseisella veikkauksella voittaa rahaa {:.2f} euroa.".format(voittosumma))
            else:
                print("Kyseista tulosta ei loydy hakemistosta.")
        except:
            print("Annoit virheellisen rahasumman")
        jatketaanko = input("Haluatko jatkaa (1 = kylla, 0 = ei)?\n")
        if jatketaanko == "0":
            break
    
    
main()