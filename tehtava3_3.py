'''
Created on 12.6.2019

@author: Lotta Ketoja
'''
import random

def main():
    siemenluku = int(input("Valitse aloitusluku ohjelman arvontaa varten\n"))
    random.seed(siemenluku)
    oikea_vastaus = random.randint(1,211)
    laskuri = 0
    while True:
        while True:
            arvaus = int(input("Anna seuraava arvaus.\n"))
            laskuri += 1
            if arvaus < 1 or arvaus > 211:
                print("Luvun taytyy olla valilta 1 - 211.")
            else:
                break
        if arvaus < oikea_vastaus:
            print("Ehei, britit ovat hitaampia!")
        elif arvaus > oikea_vastaus:
            print("Ehei, britit ovat nopeampia!")
        else:
            print("Osuit oikeaan, eroprosessi alkaa", arvaus, "paivan kuluttua.")
            print("Kaytit", laskuri, "arvauskertaa.")
            break
        
        
main()