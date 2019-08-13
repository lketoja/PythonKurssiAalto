def main():
    tiedosto = avaa_tiedosto()
    if not tiedosto:
        return
    sanakirja = tallenna_atomimassat(tiedosto)
    while True:
        molekyylikaava = input("Anna molekyylikaava.\n")
        laske_molekyylimassa(molekyylikaava, sanakirja)
        syote = input("Haluatko jatkaa (k/e)?\n")
        if syote.lower() == "e":
            print("Ohjelman suoritus paattyy.")
            break
        

def avaa_tiedosto():
    try:
        tiedoston_nimi = input("Mista tiedostosta atomimassat luetaan?\n")
        tiedosto = open(tiedoston_nimi, "r")
        return tiedosto
    except OSError:
        print("Virhe tiedoston", tiedoston_nimi, "lukemisessa. Ohjelma paattyy.")
        
            
def tallenna_atomimassat(tiedosto):
    sanakirja = {}
    for rivi in tiedosto:
        rivi = rivi.rstrip()
        lista = rivi.split(":")
        if len(lista) != 2:
            print("Virheellinen rivi:", rivi)
        else:
            try:
                atomimassa = float(lista[1])
                sanakirja[lista[0]] = atomimassa
            except ValueError:
                print("Rivilla virheellinen atomimassa:", rivi)
            
    return sanakirja

def laske_molekyylimassa(molekyylikaava, sanakirja):
    alkuaineet = molekyylikaava.split("-")
    kokonaismassa = 0
    for alkuaine in alkuaineet:
        alkuaine = alkuaine.split(":")
        
        if alkuaine[0] not in sanakirja:
            print("Alkuaineen atomimassa puuttuu:", alkuaine[0])
            return
        
        if len(alkuaine) > 2:
            print("Virheellinen molekyylikaava.")
            return
        
        if len(alkuaine)==1: 
            kokonaismassa += sanakirja[alkuaine[0]]
        else: 
            try:
                kerroin = int(alkuaine[1])
            except ValueError:
                print("Virheellinen molekyylikaava.")
                return
            kokonaismassa += sanakirja[alkuaine[0]] * kerroin
    print("Yhdisteen", molekyylikaava, "molekyylimassa on {:.2f} amu.".format(kokonaismassa))

main()
        