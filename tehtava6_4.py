'''
Created on 24.6.2019

@author: Lotta Ketoja
'''
import random
NOPPA_LKM = 5

def main():
    print("Tervetuloa pelaamaan noppapelia.")
    print("Pelissa heitetaan viisi noppaa ja lasketaan niiden yhteispisteet.")
    print("Saat heittaa haluamasi nopat kerran uudelleen.")
    print("Pisteet uusintaheittojen jalkeen ratkaisevat tuloksen.")
    alusta_noppa()
    input("Paina enter heittaaksesi noppia.\n")

def alusta_noppa():
    siemenluku = int(input("Anna siemenluku noppaa varten\n"))
    random.seed(siemenluku)


def heita_noppaa():
    SIVULKM = 6
    return random.randint(1, SIVULKM)

def heita_nopat():
    heitetyt_nopat = []
    for i in range(NOPPA_LKM):
        noppaluku = heita_noppaa()
        heitetyt_nopat.append(noppaluku)
    return heitetyt_nopat

def heita_uudelleen(uudelleen_heitettavat, nopat):
    for numero in uudelleen_heitettavat:
        for i in range(len(nopat)):
            if numero - 1 == i:
                noppaluku = heita_noppaa()
                nopat[i] = noppaluku
                continue

def tulosta_nopat_ja_laske_tulos(nopparivi):
    print("Nopat heitetty")
    print("noppa1: ", nopparivi[0], " noppa2: ", nopparivi[1], " noppa3: ", nopparivi[2], ''' nop
    pa4: ''', nopparivi[3], " noppa5: ", nopparivi[4])
    print("yhteensa", sum(nopparivi), "pistetta.")


    

main()