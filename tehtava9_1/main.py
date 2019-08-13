from opiskelija import *

kurssilainen = Opiskelija("Ville Virtanen", "123456")
print(kurssilainen)

kurssilainen.muuta_tenttiarvosana(5)
print(kurssilainen)

kurssilainen.muuta_harjoitusarvosana(4)
print(kurssilainen)

print("Kokonaisarvosana on", kurssilainen.laske_kokonaisarvosana())