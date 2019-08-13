
class Koira:
   
    ALOITTELIJA            = 1
    HARJOITTELIJA         = 2
    KESKITAITOINEN        = 3
    TAITAJA                 = 4
    TOSITAITURI            = 5
   
    TEMPPUTASOT = ["-", "aloittelija", "harjoittelija", "keskitaitoinen", "taitaja", "tositaituri"]
   
    TOSI_VASYNYT = 1
    VASYNYT = 2
    NEUTRAALI = 3
    VIRKEA = 4
    TOSI_VIRKEA = 5
   
    ENERGIATASOT = ["-", "tosi vasynyt", "vasynyt", "neutraali", "virkea", "tosi virkea"]
   
    TOSI_NALKAINEN = 1
    NALKAINEN= 2
    NEUTRAALI = 3
    KYLLAINEN = 4
    TOSI_KYLLAINEN = 5
   
    NALKATASOT = ["-", "tosi nalkainen", "nalkainen", "neutraali", "kyllainen", "tosi kyllainen"]
   
    def __init__(self, koiran_nimi):
        self.__nimi = koiran_nimi
        self.__tempputaso = 1
        self.__energia = 4
        self.__nalka = 4
        
    def juokse(self, maara):
        alkuperainen_energia = self.__energia
        if maara < self.__energia:
            self.__energia -= maara
        else:
            self.__energia = 1
        return alkuperainen_energia - self.__energia
    
    def leiki(self, maara):
        alkuperainen_kyllaisyys = self.__nalka
        if maara < self.__nalka:
            self.__nalka -= maara
        else:
            self.__nalka = 1
        return alkuperainen_kyllaisyys - self.__nalka
    
    def nuku(self, maara):
        alkuperainen_energia = self.__energia
        if maara <= 5 - self.__energia:
            self.__energia += maara
        else:
            self.__energia = 5
        return self.__energia - alkuperainen_energia
     
    def syo(self, maara):
        alkuperainen_kyllaisyys = self.__nalka
        if maara <= 5 - self.__nalka:
            self.__nalka += maara
        else:
            self.__nalka = 5
        return self.__nalka - alkuperainen_kyllaisyys
      
    def tee_temppu(self, vaikeusaste):
        if vaikeusaste <= self.__tempputaso:
            if vaikeusaste == self.__tempputaso and self.__tempputaso < 5:
                self.__tempputaso += 1
            return True
        else:
            return False
        
    def __str__(self):
        mjono = self.__nimi + ", taitotaso: " + Koira.TEMPPUTASOT[self.__tempputaso] + \
            "\nEnergia: " + Koira.ENERGIATASOT[self.__energia] + \
            "\nKyllaisyys: " + Koira.NALKATASOT[self.__nalka]
        return mjono
    
    def kerro_nimi(self):
        return self.__nimi
    
    def kerro_tempputaso(self):
        return self.__tempputaso

    def kerro_energia(self):
        return self.__energia

    def kerro_nalka(self):
        return self.__nalka
    