'''
Created on 12.6.2019

@author: Lotta Ketoja
'''
def main():
    
    while True:
        ensimmainen_luku = int(input("Anna ensimmainen tulostettava luku.\n"))
        if ensimmainen_luku < 1:
            print("Anna positiivinen luku!")
        else:
            break
    while True:
        viimeinen_luku = int(input("Anna viimeinen tulostettava luku.\n"))
        if viimeinen_luku <= ensimmainen_luku:
            print("Anna ensimmaista lukua suurempi luku!")
        else:
            break
            
    print("Hokkus pokkus valilta "+ str(ensimmainen_luku)+ " - "+ str(viimeinen_luku) +":")
    laskuri = ensimmainen_luku
    while laskuri <= viimeinen_luku:
        if laskuri % 3 == 0 and laskuri % 5 == 0:
            print("HOKKUS POKKUS!")
        elif laskuri % 5 == 0:
            print("pokkus")
        elif laskuri % 3 == 0:
            print("hokkus")
        else:
            print(laskuri)
        laskuri += 1
            
main()