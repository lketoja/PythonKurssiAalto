def main():
    tiedoston_nimi = input("Minka nimisesta tiedostosta lahtotiedot luetaan?\n")
    myynnit = {}
    try:
        tiedosto = open(tiedoston_nimi, "r")
        for rivi in tiedosto:
            rivi = rivi.rstrip()
            osat = rivi.split(":")
            if len(osat) != 2:
                print("Virhe rivissa:", rivi)
            else:
                tyontekija = osat[0]
                try:
                    myynti = float(osat[1])
                    if tyontekija in myynnit:
                        if myynti > myynnit[tyontekija]:
                            myynnit[tyontekija] = myynti
                    else:
                        myynnit[tyontekija] = myynti
                except ValueError:
                    print("Virheellinen myynti:", osat[1])
        tiedosto.close()

        # Tulostaa jokaisen parhaan myynnin
        if myynnit == {}:
            print("Tiedosto ei sisaltanyt yhtaan oikeaa myyntia.")
        else:
            print("Tyontekijoiden suurimmat myynnit:")
            print("Tyontekija      Myynti (eur)")
            print("----------------------------")
            tyontekijat = sorted(myynnit)
            for tyontekija in tyontekijat:
                print("{:<20s}{:7.2f}".format(tyontekija, myynnit[tyontekija])) 
               
    except OSError:
        print("Virhe tiedoston {:s} lukemisessa. Ohjelma paattyy.".format(tiedoston_nimi))
 
main()