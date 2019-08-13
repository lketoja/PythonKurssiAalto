# Luokka Opiskelija kuvaa eraan ohjelmointikurssin
# yhta opiskelijaa.

class Opiskelija:

    # Metodi __init__ antaa alkuarvot olion kentille.
    # Luotavalle opiskelijalle annettava nimi ja opiskelijanumero
    # annetaan metodin parametreina.

    def __init__(self, annettu_nimi, numero):
        self.__nimi = annettu_nimi
        self.__opiskelijanumero = numero
        self.__tenttiarvosana = 0
        self.__harjoitusarvosana = 0


    # Metodi palauttaa opiskelijan nimen.

    def kerro_nimi(self):
        return self.__nimi


    # Metodi palauttaa opiskelijan opiskelijanumeron.

    def kerro_opiskelijanumero(self):
        return self.__opiskelijanumero


    # Metodi palauttaa opiskelijan tenttiarvosanan.

    def kerro_tenttiarvosana(self):
        return self.__tenttiarvosana


    # Metodi palauttaa opiskelijan harjoitusarvosanan.

    def kerro_harjoitusarvosana(self):
        return self.__harjoitusarvosana


    # Metodi muuttaa opiskelijan tenttiarvosanan. Uusi arvosana
    # annetaan metodin parametrina.

    def muuta_tenttiarvosana(self, arvosana):
        if 0 <= arvosana <= 5:
            self.__tenttiarvosana = arvosana


    # Metodi muuttaa opiskelijan harjoitusarvosanan. Uusi arvosana
    # annetaan metodin parametrina.

    def muuta_harjoitusarvosana(self, arvosana):
        if 0 <= arvosana <= 4:
            self.__harjoitusarvosana = arvosana


    # Metodi laskee ja palauttaa opiskelijan kokonaisarvosanan.

    def laske_kokonaisarvosana(self):
        if self.__tenttiarvosana == 0 or self.__harjoitusarvosana == 0:
            arvosana = 0
        elif self.__tenttiarvosana == 4 or self.__tenttiarvosana == 5:
                arvosana = self.__harjoitusarvosana + 1
        elif self.__tenttiarvosana == 3:
                arvosana = self.__harjoitusarvosana
        elif self.__tenttiarvosana == 2 or self.__tenttiarvosana == 1:
            if self.__harjoitusarvosana == 1 or self.__harjoitusarvosana == 2: 
                arvosana = self.__harjoitusarvosana
            else:
                arvosana = self.__harjoitusarvosana - 1
        return arvosana


    # Metodi palauttaa merkkijonoesityksen opiskelijan tiedoista.

    def __str__(self):
        mjono = self.__nimi + ", " + self.__opiskelijanumero + \
                ", tenttiarvosana: " + str(self.__tenttiarvosana) + \
                ", harjoitusarvosana: " + str(self.__harjoitusarvosana)
        return mjono