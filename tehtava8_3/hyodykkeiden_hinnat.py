def main():
    tiedoston_nimi = input("Mista tiedostosta hintatilastot luetaan?\n")
    try:
        tiedosto = open(tiedoston_nimi, 'r')
        vuosi = input("Minka vuoden hyodykkeita haetaan?\n")
        hakusana = input("Hakusana:\n").lower()
        print("------------------------------------------------------------------------------")
        print("{:50s} {:6s}".format("Hyodyke", "Keskihinta vuonna " + vuosi + " (eur)" ))
        print("------------------------------------------------------------------------------")
        for rivi in tiedosto:
            rivi = rivi.rstrip()
            lista = rivi.split(";")
            if len(lista) != 4:
                    continue
            if lista[1].isupper():
                continue
            rivi = rivi.lower()
            if hakusana in rivi and vuosi in rivi:
                taulukko = rivi.split(";")
               
                if taulukko[2] != "keskihinta":
                    continue
                if taulukko[3] == ".":
                    taulukko[3] = "--.--"
                print("{:50s} {:>6s}".format(taulukko[1], taulukko[3]))
            
      
    except OSError:
        print("Tiedostoa ei loydy tai lukuoikeudet puuttuvat.")
        
main()