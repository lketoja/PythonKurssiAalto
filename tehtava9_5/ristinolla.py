


class Ristinolla:
    
    PELAAJA1 = 1
    PELAAJA2 = 2
    RATKAISEMATON = 3
    MERKKI1 = 1
    MERKKI2 = -1
    TYHJA = 0
    EI_LOYDY = 0
    KESKEN = 0
    KOKO = 4
    MERKIT = ['_', 'X', '0']
    
    def __init__(self, nimi1, nimi2):
        self.__pelaaja1 = nimi1
        self.__pelaaja2 = nimi2
        self.__pelilauta = []
        for i in range(Ristinolla.KOKO):
            rivi = []
            for j in range(Ristinolla.KOKO):
                rivi.append(Ristinolla.TYHJA)
            self.__pelilauta.append(rivi)
            
    def kerro_pelaaja1(self):
        return self.__pelaaja1
    
    def kerro_pelaaja2(self):
        return self.__pelaaja2
    
    def lisaa_merkki(self, x_koord, y_koord, pelaaja):
        if x_koord > Ristinolla.KOKO -1 or x_koord < 0:
            return False
        if y_koord > Ristinolla.KOKO -1 or y_koord < 0:
            return False
        vaakarivi = Ristinolla.KOKO - 1 - y_koord
        pelilaudan_merkki = self.__pelilauta[vaakarivi][x_koord]
        if pelilaudan_merkki == 1 or pelilaudan_merkki == 2:
            return False
        self.__pelilauta[vaakarivi][x_koord] = pelaaja
        return True
    
    def peli_paattynyt(self):
        if self.onko_ruudukko_taynna():
            return Ristinolla.RATKAISEMATON
        vaakavoittaja = self.onko_voitto_vaakarivilla()
        if vaakavoittaja:
            return vaakavoittaja
        pystyvoittaja = self.onko_voitto_pystyrivilla()
        if pystyvoittaja:
            return pystyvoittaja
        lavistajavoittaja = self.onko_voitto_lavistajalla()
        if lavistajavoittaja:
            return lavistajavoittaja
        return Ristinolla.KESKEN
        
            
    
    def onko_ruudukko_taynna(self):
        for i in range(Ristinolla.KOKO):
            for j in range(Ristinolla.KOKO):
                if self.__pelilauta[i][j] == Ristinolla.TYHJA:
                    return False
        return True
    
    def onko_voitto_vaakarivilla(self):
        voittaja = None
        for i in range(Ristinolla.KOKO):
            if self.__pelilauta[i][0] == Ristinolla.TYHJA:
                continue
            else:
                voittaja = self.__pelilauta[i][0]
                for j in range(Ristinolla.KOKO-1):
                    if self.__pelilauta[i][0] != self.__pelilauta[i][j+1]:
                        voittaja = None
                        break
            if voittaja:
                return voittaja
    
    def onko_voitto_pystyrivilla(self):
        voittaja = None
        for j in range(Ristinolla.KOKO):
            if self.__pelilauta[0][j] == Ristinolla.TYHJA:
                continue
            else:
                voittaja = self.__pelilauta[0][j]
                for i in range(Ristinolla.KOKO-1):
                    if self.__pelilauta[0][j] != self.__pelilauta[i+1][j]:
                        voittaja = None
                        break
            if voittaja:
                return voittaja
    
    def onko_voitto_lavistajalla(self):
        ylhaalta_alas = True
        if self.__pelilauta[0][0] != Ristinolla.TYHJA:
            j=0
            for i in range(Ristinolla.KOKO - 1):
                if self.__pelilauta[0][0] != self.__pelilauta[i+1][j+1]:
                    ylhaalta_alas = False
                    break
                j += 1
        else:
            ylhaalta_alas = False 
        
        if ylhaalta_alas:
            return self.__pelilauta[0][0]
        
        alhaalta_ylos = True
        if self.__pelilauta[Ristinolla.KOKO - 1][0] != Ristinolla.TYHJA:
            i = Ristinolla.KOKO - 1
            for j in range(Ristinolla.KOKO - 1):
                if self.__pelilauta[Ristinolla.KOKO - 1][0] != self.__pelilauta[i-1][j]:
                    alhaalta_ylos = False
                    break
                i -= 1
        else: 
            alhaalta_ylos = False
            
        if alhaalta_ylos:
            return self.__pelilauta[Ristinolla.KOKO-1][0]
        
    def __str__(self):
        mjono = ""
        for i in range(Ristinolla.KOKO): 
            for j in range(Ristinolla.KOKO - 1):
                mjono += Ristinolla.MERKIT[self.__pelilauta[i][j]]
            mjono += Ristinolla.MERKIT[self.__pelilauta[i][Ristinolla.KOKO - 1]] + "\n"
        return mjono   
            
            
        

        