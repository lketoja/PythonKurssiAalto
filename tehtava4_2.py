'''
Created on 14.6.2019

@author: Lotta Ketoja
'''
def muunna(solmut):
    if solmut < 0:
        print("Nopeus ei voi olla negatiivinen!")
    else:
        kmh_nopeus = solmut*1.852
        ms_nopeus = kmh_nopeus/3.6
        print(solmut, "solmua on", kmh_nopeus, "km/h ja", ms_nopeus, "m/s.")
    
def main():
    print("Ohjelma muuntaa solmut yksikoihin km/h ja m/s.")
    while True:        
        nopeus_solmuina = int(input("Mika on nopeus solmuissa?\n"))
        muunna(nopeus_solmuina)
        jatko = input("Haluatko jatkaa (1 = kylla / 0 = ei)?\n")
        if jatko == "0":
            print("Ohjelma paattyy.")
            break
        
main()