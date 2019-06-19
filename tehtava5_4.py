'''
Created on 18.6.2019

@author: Lotta Ketoja
'''

import random

# Maaritellaan vakioita, joiden avulla on helppo kasitella tietokoneen
# ja kayttajan valintoja seka pelin voittajaa.

KIVI = 1
SAKSET = 2
PAPERI = 3
VALINNAT = ["tyhja", "kivi", "sakset", "paperi"]
VALINTA_LKM = 3
TIETOKONE = -1
PELAAJA = 1
TASAPELI = 0

# Funktio alustaa tietokoneen arpomisessa kayttaman
# satunnaislukugeneraattorin kayttajan antamalla luvulla.

def  main():
    tee_alustus()
    while True:
        koneen_valinta = arvo_tietokoneen_valinta()
        pelaajan_valinta = pyyda_kayttajan_valinta()
        voittaja = valitse_voittaja(pelaajan_valinta, koneen_valinta)
        print("Tietokoneen valinta oli", VALINNAT[koneen_valinta])
        print("Sinun valintasi oli", VALINNAT[pelaajan_valinta])
        if voittaja == TASAPELI:
            print("Peli ei viela ratkennut, yrita uudelleen.")
        else:
            if voittaja == TIETOKONE:
                print("Tietokone voitti!")
            else:
                print("Sina voitit!")
            break
        
def tee_alustus():
    print("Tervetuloa pelaamaan kivi-sakset-paperi-pelia.")
    rivi = input("Anna siemenluku tietokoneen arpomista varten.\n")
    siemenluku = int(rivi)
    random.seed(siemenluku)


# Funktio arpoo ja palauttaa tietokoneen valinnan (kivi, sakset tai
# paperi) satunnaislukugeneraattorin avulla.

def arvo_tietokoneen_valinta():
    return random.randint(1, VALINTA_LKM)

def pyyda_kayttajan_valinta():
    print("Valitse joku seuraavista:")
    print("1 = KIVI")
    print("2 = SAKSET")
    print("3 = PAPERI")
    while True:
        kayttajan_valinta = int(input("Anna valintasi.\n"))
        if kayttajan_valinta > 0 and kayttajan_valinta < 4:
            break
    return kayttajan_valinta

def valitse_voittaja(pelaajan_valinta, koneen_valinta):
    if pelaajan_valinta == KIVI:
        if koneen_valinta == SAKSET:
            return PELAAJA
        elif koneen_valinta == PAPERI:
            return TIETOKONE
        else:
            return TASAPELI
    elif pelaajan_valinta == SAKSET:
        if koneen_valinta == KIVI:
            return TIETOKONE
        elif koneen_valinta == PAPERI:
            return PELAAJA
        else:
            return TASAPELI 
    elif pelaajan_valinta == PAPERI:
        if koneen_valinta == SAKSET:
            return TIETOKONE
        elif koneen_valinta == KIVI:
            return PELAAJA
        else:
            return TASAPELI
        
main()
        




