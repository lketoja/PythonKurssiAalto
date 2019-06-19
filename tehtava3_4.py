
def main():
    kiitoradan_pituus = int(input("Mika on kiitoradan pituus (m)?\n"))
    aika_nollasta_sataan = float(input("Kuinka monta sekuntia lentokoneelta kestaa kiihdyttaa 0-100 km/h?\n"))
    lentoonlahtonopeus = float(input("Mika on lentokoneen lentoonlahtonopeus (km/h)?\n"))/3.6
    kiihtyvyys = 100 / 3.6 / aika_nollasta_sataan
    
    aika = 0.0
    nopeus = 0.00
    matka = 0.00
    print("{:>4s} {:>10s} {:>10s}".format("t (s)", "v (km/h)", "matka (m)"))
    while True:
        nopeus = kiihtyvyys * aika
        matka = 0.5 * kiihtyvyys * aika ** 2
        print("{:4.1f} {:10.2f} {:10.2f}".format(aika, nopeus * 3.6 , matka))
        if matka > kiitoradan_pituus:
            print("Lentokone ei ehdi saavuttaa lentoonlahtonopeutta")
            print("Tarvitaan pidempi kiitorata")
            break
        elif nopeus > lentoonlahtonopeus:
            print("Kiitorata on tarpeeksi pitka lentokoneelle")
            break
        aika += 5
        
main()