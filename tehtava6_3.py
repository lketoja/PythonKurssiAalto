'''
Created on 24.6.2019

@author: Lotta Ketoja
'''

def main():
    syote = input("Anna opiskelijan harjoituspisteet yhdella rivilla.\n")
    pistelista = luo_pistelista(syote)
    kurssi_suoritettu = tarkista_muut_minimit(pistelista)
    if not kurssi_suoritettu:
        print("Opiskelija ei tayttanyt pakollisten kierrosten minimipistevaatimuksia.")
        return 
    yhteispisteet = laske_yhteispisteet(pistelista)
    viimeinen_minimi_ylitetty = tarkista_viimeinen_minimi(pistelista)
    arvosana = laske_arvosana(yhteispisteet, viimeinen_minimi_ylitetty)
    print("Yhteispisteet: " + str(yhteispisteet) + ", arvosana: " + str(arvosana))

def luo_pistelista(luettu_rivi):
    lista = luettu_rivi.split()
    for i in range(len(lista)):
        lista[i] = int(lista[i])
    return lista

def tarkista_viimeinen_minimi(pistelista):
    if pistelista[-1] >= 600:
        return True
    else:
        return False
    
def tarkista_muut_minimit(pistelista):
    if pistelista[0] < 100:
        return False
    if pistelista[1] < 365:
        return False
    if pistelista[2] < 285:
        return False
    for i in range(3,8):
        if pistelista[i] < 325:
            return False
    if pistelista[8] < 310:
        return False
    return True

def laske_yhteispisteet(pistelista):
    return sum(pistelista)

def laske_arvosana(yhteispisteet, viimeinen_minimi_ylitetty):
    if yhteispisteet < 2690:
        return 0
    if yhteispisteet < 3450:
        return 1
    if yhteispisteet < 4200:
        return 2
    if not viimeinen_minimi_ylitetty:
        return 2
    if yhteispisteet < 5000:
        return 3
    if yhteispisteet < 5800:
        return 4
    return 5

main()