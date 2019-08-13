
class Laivanupotus:
    OSUMA = 1
    OHI = 0
    ULKONA = -1
    
    def __init__(self, pelaajan_nimi, toisen_pelaajan_laivat):
        self.__nimi = pelaajan_nimi
        self.__kentta = ["_" for i in range(101)]
        self.__laivat = toisen_pelaajan_laivat
    
    def kerro_pelaaja(self):
        return self.__nimi
    
    def ammu(self, paikka):
        if paikka < 1 or paikka > 100 or self.__kentta[paikka] != "_":
            return Laivanupotus.ULKONA
        elif paikka in self.__laivat:
            self.__kentta[paikka] = Laivanupotus.OSUMA
            return Laivanupotus.OSUMA
        else:
            self.__kentta[paikka] = Laivanupotus.OHI
            return Laivanupotus.OHI
        
    def peli_paattynyt(self):
        for paikka in self.__laivat:
            if self.__kentta[paikka] == "_":
                return False
        return True
    
    def __str__(self):
        mjono = ""
        k = 1
        for i in range(10):
            for j in range(9):
                if self.__kentta[k] == Laivanupotus.OSUMA:
                    mjono += "X "
                elif self.__kentta[k] == Laivanupotus.OHI:
                    mjono += "O "
                else:
                    mjono += "_ "
                k += 1
            if self.__kentta[k] == Laivanupotus.OSUMA:
                mjono += "X\n"
            elif self.__kentta[k] == Laivanupotus.OHI:
                mjono += "O\n"
            else:
                mjono += "_\n"
            k += 1
        return mjono