import datetime

def muunna_paivamaarateksti_paivamaaraksi(paivamaara_tekstina):
    """
    Parametri paivamaara_tekstina on merkkijono, joka annetaan muodossa
    DD.MM.YYYY, eli esimerkiksi 17.5.2019

    Palauttaa paivamaaran (tarkalleen datetime.date-olennon)
    """
    pvm_lista = paivamaara_tekstina.split(".")
    paiva     = int(pvm_lista[0])
    kuukausi  = int(pvm_lista[1])
    vuosi     = int(pvm_lista[2])
    paivamaara = datetime.date(year = vuosi, month = kuukausi, day = paiva)
    return paivamaara

def tulosta_tiedoston_sisalto(tiedostonimi):
    """
    Tulostaa tiedostonimi-nimisen tiedoston sisallon
    """
    print()
    print("Luomasi tiedoston sisalto nayttaa seuraavalta:")
    print("----------------------------------------------------------------------------------------------------")
    tarkasteltava_tiedosto = open(tiedostonimi, 'r')
    for line in tarkasteltava_tiedosto:
        print(line, end='')
    tarkasteltava_tiedosto.close()

def main():
    tiedoston_nimi = input("Minka niminen tiedosto luodaan askelmaarien tallentamiseksi?\n")
    askelmaaratiedosto = open(tiedoston_nimi, 'w')
    paivamaara_tekstina = input("Mista paivasta aloitetaan? Anna paiva muodossa DD.MM.YYYY:\n")
    paivamaara = muunna_paivamaarateksti_paivamaaraksi(paivamaara_tekstina)
    print("Anna kavelemasi / juoksemasi askeleet paivakohtaisesti. Lopeta tyhjalla rivilla.")
    laskuri = 0
    summa = 0
    while True:
        askelmaara = input("Anna askelmaara paivalle {}: ".format(paivamaara))
        if not askelmaara:
            break
        laskuri += 1
        summa += int(askelmaara)
        askelmaaratiedosto.write(str(paivamaara) + ": " + askelmaara + "\n")
        paivamaara += datetime.timedelta(days = 1)
    askelmaaratiedosto.close()
    print("----------------------------------------------------------------------------------------------------")
    if laskuri>0:
        keskiarvo = summa // laskuri
        print("Askelmaarat tallennettu onnistuneesti tiedostoon " + tiedoston_nimi)
        print("Tallennettiin", laskuri, "paivan askeleet, joita oli yhteensa", summa, "ja keskimaarin paivassa {}.".format(keskiarvo))
    else:
        keskiarvo = 0
        print("Askelmaarat tallennettu onnistuneesti tiedostoon " + tiedoston_nimi)
        print("Tallennettiin", laskuri, "paivan askeleet.")
   
    
    tulosta_tiedoston_sisalto(tiedoston_nimi)

main()
