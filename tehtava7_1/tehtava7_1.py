'''
Created on 26.6.2019

@author: Lotta Ketoja
'''
def main():
    name = input("Minka nimisesta tiedostosta lahtotiedot luetaan?\n")
    
    count = 0
    try:
        pricefile = open(name, "r")
        budjetti = float(input("Mika on budjettisi evasleivalle euroissa?\n"))
        for line in pricefile:
            line = line.rstrip()
            price = float(line)
            if price <= budjetti:
                count += 1
        pricefile.close()
        if count == 0:
            print("Yksikaan tuote ei sovi", budjetti, "euron budjettiin.")
        else:
            print(count, "tuotetta sopii", budjetti, "euron budjettiin.")
    except OSError:
        print("Tiedoston {:s} lukemisessa tuli virhe. Ohjelma paattyy.".format(name))
    except ValueError:
        print("Tiedostossa {:s} on virheellinen luku. Ohjelma paattyy".format(name))

main()