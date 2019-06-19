'''
Created on 17.6.2019

@author: Lotta Ketoja
'''

def main():
    lkm = int(input("Kuinka monen tuotteen hinnat annat?\n"))
    hinnat = [0.0] * lkm
    for i in range(lkm):
        luettu_hinta = float(input("Anna seuraavan tuotteen hinta (eur).\n"))
        hinnat[i] = luettu_hinta

    print("Alennetut hinnat")
    RAJA = 50.0
    PIENI_ALENNUS = 10.0
    SUURI_ALENNUS = 30.0

    summa = 0
    for hinta in hinnat:
        if hinta < RAJA:
            alennettu_hinta = (100 - PIENI_ALENNUS) / 100 * hinta 
        else:
            alennettu_hinta = (100 - SUURI_ALENNUS) / 100 * hinta
        print("{:.2f} eur".format(alennettu_hinta))
        summa += alennettu_hinta
    
    print("Alennetut hinnat yhteensa: {:.2f} eur.".format(summa))
    

main()