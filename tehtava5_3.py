'''
Created on 17.6.2019

@author: Lotta Ketoja
'''
def main():
    print("Ohjelma laskee hygieniatuotteiden kayton kustannukset.")
    vuosikustannukset= []
    hygieniatuotteet = ["hammastahna", "shampoo", "suihkusaippua", "partavaahto"]
    for tuote in hygieniatuotteet:
        kpl_hinta = lue_hinta(tuote)
        kesto_vko = lue_kesto(tuote)
        montako_vuodessa = laske_vuodessa_tarvittavat(kesto_vko)
        vuosikulu = vuosikulut(montako_vuodessa, kpl_hinta)
        vuosikustannukset.append(vuosikulu)
    
    print("Hygieniatuotteiden kayton kustannukset vuodessa ovat")
    print("Tuote     vuosikulut (eur)")
    for i in range(len(hygieniatuotteet)):
        print("{:13s} {:6.2f}".format(hygieniatuotteet[i], vuosikustannukset[i]))
        
    

def laske_vuodessa_tarvittavat(kesto_vko):
    return 52 / kesto_vko

def vuosikulut(montako_vuodessa, kpl_hinta):
    return montako_vuodessa * kpl_hinta

def lue_hinta(tuotenimi):
    print("Paljonko maksaa uusi", tuotenimi, "(eur)?")
    while True:
        hinta = float(input(""))
        if hinta >= 0:
            break
        else:
            print("Anna positiivinen hinta!")
    return hinta

def lue_kesto(tuotenimi):
    print("Montako viikkoa", tuotenimi, "kesti?")
    while True:
        kesto = int(input(""))
        if kesto > 0:
            break
        else:
            print("Anna viikot uudelleen!")
    return kesto

main()