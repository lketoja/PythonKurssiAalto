
def main():
    print("Ohjelma laskee ja visualisoi ilmanlaatua.")
    tiedoston_nimi = input("Minka nimisesta tiedostosta lahtotiedot luetaan?\n")
    try:
        tiedosto = open(tiedoston_nimi, "r")
    except OSError:
        print("Tiedoston lukemisessa tuli virhe.")
        return 
    
    matriisi = lue_tiedot_matriisiin(tiedosto)
    kolmikko = pilko_tiedot_listoiksi(matriisi)
    paikkakunnat = kolmikko[0]
    ajankohdat = kolmikko[1]
    ilmanlaadut = kolmikko[2]
    print(paikkakunnat)
    print(ajankohdat)
    print(ilmanlaadut)
    
    
    keskiarvot = laske_kaikki_keskiarvot(matriisi)
    maksimit = etsi_kaikki_maksimit(matriisi)
    
        
    
        
    for i in range(5):
        print("{:10.1f}{:10d}".format(keskiarvot[i], maksimit[i]))
 
    
def lue_tiedot_matriisiin(tiedosto):
    matriisi = []
    for rivi in tiedosto:
        rivi = rivi.rstrip()
        lista = rivi.split(",")
        matriisi.append(lista)
    return matriisi

def pilko_tiedot_listoiksi(matriisi):
    paikkakunnat = []
    ajankohdat = []
    ilmanlaadut = []
    for j in range(1, len(matriisi[0])):
        paikkakunnat.append(matriisi[0][j])
    for i in range(1, len(matriisi)):
        ajankohdat.append(matriisi[i][0])
    for i in range(1, len(matriisi)):
        rivi = []
        for j in range(1, len(matriisi[0])):
            rivi.append(matriisi[i][j])
        ilmanlaadut.append(rivi)
    return [paikkakunnat, ajankohdat, ilmanlaadut]

def muuta_ilmanlaadut_kokonaisluvuiksi(matriisi):
    for i in range(1, len(matriisi)):
        for j in range(1, len(matriisi[0])):
            matriisi[i][j]=int(matriisi[i][j])

def laske_kaikki_keskiarvot(matriisi):           
    keskiarvot = []
    for i in range(1, len(matriisi[0])):
        ka = laske_keskiarvo(matriisi, i)
        keskiarvot.append(ka)
    return keskiarvot

def etsi_kaikki_maksimit(matriisi):
    maksimit = []
    for i in range(1, len(matriisi[0])):
        maks = etsi_maksimi(matriisi, i)
        maksimit.append(maks)
    return maksimit

def laske_keskiarvo(matriisi, pystyrivi):
    summa = 0
    laskuri = 0
    for i in range(1, len(matriisi)):
        summa += matriisi[i][pystyrivi]
        laskuri += 1
    return summa / laskuri


def etsi_maksimi(matriisi, pystyrivi):
    lista = []
    for i in range(1, len(matriisi)):
        lista.append(matriisi[i][pystyrivi])
    return max(lista)

main()