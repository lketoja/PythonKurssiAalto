

def main():
    print("Ohjelma laskee ja visualisoi ilmanlaatua.")
    tiedoston_nimi = input("Minka nimisesta tiedostosta lahtotiedot luetaan?\n")
    try:
        tiedosto = open(tiedoston_nimi, "r")
    except OSError:
        print("Tiedoston lukemisessa tuli virhe.")
        return
    paikkakuntien_lukumaara = int(input("Kuinka monta paikkakuntaa tiedostossa on?\n"))
    
    
    rivi = tiedosto.readline().rstrip()
    paikkakunnat = rivi.split(",")
    paikkakunnat = paikkakunnat[1:] #poistetaan 'Aikaleima' listasta
    
    #tallennetaan ilmanlaatuindeksit listaan, jonka kukin alkio on toinen lista,
    #joka sisältää yhden mittausajankohdan ilmanlaatuindeksit
    aikaleimat = []
    ilmanlaadut = []
    for rivi in tiedosto:
        lista = rivi.rstrip().split(",")
        aikaleimat.append(lista[0])
        aikaleiman_ilmanlaadut = []
        if len(lista) != paikkakuntien_lukumaara + 1:
            print("Virheellinen rivi:", rivi, end = '')
            aikaleiman_ilmanlaadut = [0 for i in range(paikkakuntien_lukumaara)]
        else:
            for i in range(1,paikkakuntien_lukumaara + 1):
                try:
                    aikaleiman_ilmanlaadut.append(int(lista[i]))
                except:
                    print("Virheellinen arvo rivilla:", rivi, end = '') 
                    aikaleiman_ilmanlaadut.append(0) 
        ilmanlaadut.append(aikaleiman_ilmanlaadut)
    
    print()
    print("Tiedosto on luettu loppuun.")
    print()
    
    tulostetaanko = onko_virheettomia_riveja(ilmanlaadut)
    
    if not tulostetaanko:
        print("Ei tarpeeksi tietoja tilastointiin. Ohjelma paattyy.")
    else:
        #tallennetaan ilmanlaatuindeksit sanakirjaa siten, että avaimena toimii paikkakunta,
        #ja arvona lista kyseisen paikkakunnan ilmanlaaduista
        paikkakunta_ilmanlaadut_dict = {}
        for i in range(len(paikkakunnat)):
            paikkakunnan_ilmanlaadut = []
            for j in range(len(aikaleimat)):
                paikkakunnan_ilmanlaadut.append(ilmanlaadut[j][i])
            paikkakunta_ilmanlaadut_dict[paikkakunnat[i]] = paikkakunnan_ilmanlaadut
    
        tulosta_keskiarvot_ja_maksimit(paikkakunnat, paikkakunta_ilmanlaadut_dict)
            
        print("Mittauspaikkojen ilmanlaatu")
        print("---------------------------")
        
        print("{:16s}  ".format("Aika"), end = '')
        for paikkakunta in paikkakunnat:
            print("{:15s}  ".format(paikkakunta), end = '')
        print()
               
        for i in range(len(ilmanlaadut)):
            print("{:16s}  ".format(aikaleimat[i]), end = '')
            for j in range(len(ilmanlaadut[0])):
                print("{:15s}  ".format(ilmanlaatu_sanalliseksi(ilmanlaadut[i][j])), end = '')
            print()

def tulosta_keskiarvot_ja_maksimit(paikkakunnat, paikkakunta_ilmanlaadut_dict):
    print("Tulostetaan ilmanlaadun indeksien keskiarvot ja maksimit.")
    print("{:15s}  {:9s}  {:7s}  {:15s}".format("Mittauspaikka", "keskiarvo", "maksimi", "ilmanlaatu"))
    for i in range(len(paikkakunnat)):
        lista = paikkakunta_ilmanlaadut_dict[paikkakunnat[i]]
        mittaustulosten_lukumaara = 0
        for mittaustulos in lista:
            if mittaustulos != 0:
                mittaustulosten_lukumaara += 1
        keskiarvo = sum(lista)/mittaustulosten_lukumaara
        print("{:15s}  {:<9.1f}  {:<7d}  {:15s}".format(paikkakunnat[i], keskiarvo, max(lista), ilmanlaatu_sanalliseksi(keskiarvo)))
    print() 
    
    
def ilmanlaatu_sanalliseksi(ilmanlaatu):
    if ilmanlaatu == 0:
        return "-"
    elif ilmanlaatu <= 50:
        return "Hyva"
    elif ilmanlaatu <= 75:
        return "Tyydyttava"
    elif ilmanlaatu <= 100:
        return "Valttava"
    elif ilmanlaatu <= 150:
        return "Huono"
    else:
        return "Erittain huono"
    
def onko_virheettomia_riveja(ilmanlaadut):
    for rivi in ilmanlaadut:
        if rivi and max(rivi) != 0:
            return True
    return False
    
main()