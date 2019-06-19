def main():
    while True:
        lukujen_maara = int(input("Montako lukua annetaan?"))
        if lukujen_maara < 1:
            print("Anna positiivinen arvo!")
        else:
            break
    parilliset=0
    parittomat=0
    print("Anna luvut omilla riveillaan.")
    for i in range(lukujen_maara):
        luku = int(input(""))
        if luku % 2 == 0:
            parilliset += 1
        else:
            parittomat += 1
    print("Lukuja annettiin", lukujen_maara,"kpl.")
    print("Niista", parilliset, "on parillisia ja", parittomat, "parittomia.")
    
main()