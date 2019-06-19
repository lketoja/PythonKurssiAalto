'''
Created on 13.6.2019

@author: Lotta Ketoja
'''

def laske(nimi, ika):
    if ika == 18:
        print(nimi+", tiesit varmaan, etta olet tasan 18-vuotias?")
    elif ika > 18:
        print(nimi+", taytit kahdeksantoista " + str(ika - 18) + " vuotta sitten.")
    elif ika <18:
        print(nimi+ ", taytat kahdeksantoista " + str(18 - ika) + " vuoden paasta.")


def main():
    nimeni = input("Mika on nimesi?\n")
    ikani = int(input("Mika on ikasi?\n"))
    laske(nimeni, ikani)

main()
