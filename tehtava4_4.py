'''
Created on 14.6.2019

@author: Lotta Ketoja
'''
import math

def main():
    print("Taman ohjelman avulla voit laskea kappaleen")
    print("hitausmomentin ja pyorimisenergian.")
    while True:
        print("Valitse kappale:")
        print("1. Sylinteri (umpinainen)")
        print("2. Sylinteri (ontto)")
        kappale = input("3. Pallo (umpinainen)\n")
        if kappale == "1" or kappale == "2" or kappale == "3":
            break
    pyorimisnopeus = float(input("Mika on pyorimisnopeus (rpm)?\n"))
    kulma_nopeus = kulmanopeus(pyorimisnopeus)
    if kappale == "1":
        hitausmomentti = laske_sylinterin_hitausmomentti()
    elif kappale == "2":
        hitausmomentti = laske_onton_sylinterin_hitausmomentti()
    elif kappale == "3":
        hitausmomentti = laske_pallon_hitausmomentti()
    pyorimis_energia = pyorimisenergia(hitausmomentti, kulma_nopeus)
    print("Hitausmomentti on {:.2f} kgm**2".format(hitausmomentti))
    print("ja pyorimisenergia {:.2f} J.".format(pyorimis_energia))
    
        
def laske_sylinterin_hitausmomentti():
    sade = float(input("Mika on sylinterin sade (m)?\n"))
    massa = float(input("Mika on sylinterin massa (kg)?\n"))
    return 1/2 * massa * sade**2

def laske_onton_sylinterin_hitausmomentti():
    r1 = float(input("Mika on sylinterin sisasade (m)?\n"))
    r2 = float(input("Mika on sylinterin ulkosade (m)?\n"))
    m = float(input("Mika on sylinterin massa (kg)?\n"))
    return 1/2 * m * (r1**2 + r2**2)

def laske_pallon_hitausmomentti():
    r = float(input("Mika on pallon sade (m)?\n"))
    m = float(input("Mika on pallon massa (kg)?\n"))
    return 2/5 * m * r**2

def kulmanopeus(krs_minuutissa):
    return krs_minuutissa * 2 * math.pi / 60

def pyorimisenergia(hitausmomentti, kulmanopeus):
    return 1/2 * hitausmomentti * kulmanopeus**2

main()

