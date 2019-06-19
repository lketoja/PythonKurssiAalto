# coding=<encoding name>

def main():
    paivien_lkm = int(input("Kuinka monen paivan nukkumisajat annat?"))
    tunnit = 0
    minuutit = 0
    
    laskuri = 0
    while laskuri < paivien_lkm:
        paivan_tunnit = int(input("Montako tuntia nukuit seuraavana paivana?"))
        paivan_minuutit = int(input("Montako minuuttia sen paalle?"))
        if paivan_tunnit<0 or paivan_minuutit<0:
            print("Tuntien ja minuuttien taytyy olla vahintaan 0!")
        else:    
            tunnit += paivan_tunnit
            minuutit += paivan_minuutit
            laskuri += 1
        
    lisatunnit = minuutit // 60
    tunnit += lisatunnit
    minuutit = minuutit % 60
    
    print("Nukuit yhteensa", tunnit, "h", minuutit, "min.")
    
main()
    