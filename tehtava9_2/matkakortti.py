# Y1KESA 2019
# Luokka kuvaa matkakorttia
# Luokkaa kaytetaan tehtavassa 9.2
# Kirjoittanut Vilma Kahri


class Matkakortti:
    
    AIKUINEN = 1
    LAPSI = 2
    TYYPIT = ["tyhja", "aikuinen", "lapsi"]
   
    def __init__(self,omistajan_nimi, kortin_tyyppi):
        self.__omistaja = omistajan_nimi
        self.__tyyppi = kortin_tyyppi
        self.__saldo = 0.0
        
    # Metodi palauttaa matkakortin omistajan
    def kerro_omistaja(self):
        return self.__omistaja
    
    # Metodi palauttaa matkakortin tyypin
    def kerro_tyyppi(self):
        return self.__tyyppi
    
    # Metodi palauttaa matkakortin saldon
    def kerro_saldo(self):
        return self.__saldo
            
    # Metodi muuttaa kortin tyyppia annetun tyypin mukaan, 
    # kayttaen apunaan TYYPIT-listaa
    def muuta_tyyppi(self, uusi_tyyppi):
        if self.__tyyppi != uusi_tyyppi:
            self.__tyyppi = uusi_tyyppi
    
    # Metodi lisaa saldoa matkakortille. Se tarkistaa, etta
    # lisattava maara on positiivinen
    def lisaa_saldoa(self, maara):
        if maara > 0.0:
            self.__saldo += maara
    
    # Metodi nollaa matkakortin saldon
    def nollaa_saldo(self):
        self.__saldo = 0.0
        
    # Metodi tarkistaa, onko lipulla tarpeeksi saldoa lipun ostamiseen
    # Jos on, lipun hinta vahennetaan saldosta.
    # Metodi palauttaa onnistuiko lipun osto
    def osta_lippu(self,lipun_hinta):
        if self.__saldo >= lipun_hinta and lipun_hinta>0.0:
            self.__saldo -= lipun_hinta
            return True
        else:
            return False
        
    # Metodi palauttaa merkkijonon, joka sisaltaa
    # matkakortin omistajan, tyypin ja saldon.
    def __str__(self):
        mjono = "Henkilon {:s} matkakortti: tyyppia {:s}, saldo {:.2f} euroa.".format(self.__omistaja,Matkakortti.TYYPIT[self.__tyyppi], self.__saldo)
        return mjono