'''
Created on 17.6.2019

@author: Lotta Ketoja
'''
def main():
    print("Anna laskuvarjohyppaajan putoamisnopeus. Tyypillinen nopeus")
    putoamisnopeus = int(input("mahallaan putoamiselle on noin 54 m/s ja pystysuoraan 90 m/s.\n"))
    massa = int(input("Anna hyppaajan massa (kg).\n"))
    
    hyppaajaan_vaikuttava_voima = laske_voima(massa, putoamisnopeus)
    vastaava_massa = laske_vastaava_massa(hyppaajaan_vaikuttava_voima)
    
    print("Laskuvarjon avaus aiheuttaa hyppaajalle", round(hyppaajaan_vaikuttava_voima) ,"Newtonin voiman.")
    print("Voima vastaa", round(vastaava_massa), "kilogramman massaa.")
def laske_voima(massa, alkunopeus):
    nopeuden_muutos = alkunopeus - 5.0
    aika = 3.0
    return massa * nopeuden_muutos / aika

def laske_vastaava_massa(voima):
    return voima / 9.81

main()