'''
Created on 14.6.2019

@author: Lotta Ketoja
'''
def main():
    while True:
        opintotukikuukaudet = int(input("Monelleko kuukaudelle olet saanut opintotukea?\n"))
        if opintotukikuukaudet > 0 and opintotukikuukaudet < 13:
            break
    vanhat_tulot = float(input("Paljonko olet ansainnut tahan mennessa?\n"))
    while True:
        tuntipalkka = float(input("Mika on tuntipalkkasi?\n"))
        if tuntipalkka > 0:
            break
    while True:
        viikot = int(input("Montako viikkoa vuodesta on jaljella?\n"))
        if viikot > 0 and viikot < 53:
            break
    tuloraja = laske_tuloraja(opintotukikuukaudet)
    viikkotunnit = laske_viikkotunnit(vanhat_tulot, tuntipalkka, tuloraja, viikot)
    print("Voit tehda toita korkeintaan {:.2f} h/vko.".format(viikkotunnit))

def laske_tuloraja(opintotukikuukaudet):
    tuettomat_kuukaudet = 12 - opintotukikuukaudet
    return opintotukikuukaudet * 667 + tuettomat_kuukaudet * 1990

def laske_viikkotunnit(vanhat_tulot, tuntipalkka, tuloraja, loppuvuoden_viikot):
    if vanhat_tulot > tuloraja + 222:
        return 0.0
    sallittu_tienesti = tuloraja + 222 - vanhat_tulot
    sallittu_viikkotienesti = sallittu_tienesti / loppuvuoden_viikot
    sallittu_tuntimaara = sallittu_viikkotienesti / tuntipalkka
    return sallittu_tuntimaara

main()
