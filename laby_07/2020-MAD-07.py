"""
efwefjw;lf;ij'IFJLASDFCKD
"""

import random

def main():
    random.seed(9876)
    #n=int(input("podaj odleglosc do celu w krokach: "))
    #p=int(input("podaj ilosc prob: "))
    n=30
    p=2
    lista_L = [2 * (random.randint(5, 20)) for i in range(p)]
    print(lista_L)
    czy_cel=[0 for i in range (p)]
    pokonane_w_kazdej_probie=[0 for i in range (p)]
    for i in range(p):
        print(f"Proba numer {i+1}.")
        rzuty_kostka=rzucaj(lista_L[i])
        print(f"Rzuty: {rzuty_kostka}")

        pokonane, czy_cel[i]=sprawdz(rzuty_kostka,n)
        if czy_cel[i]:
            do_pokonania=0
        else:
            do_pokonania=n-pokonane
        pokonane_w_kazdej_probie[i]=pokonane
        print(f"Wykonujac {lista_L[i]} rzutow udalo sie pokonac {pokonane} krokow. Do pokonania zostalo {do_pokonania}")
    print(f"Kroki pokonane we wszystkich probach: {pokonane_w_kazdej_probie}")
    print(f"Sukces kazdej z prob: {czy_cel}")


    return

def sprawdz(rzuty_kostka, cel):
    licznik=0
    suma=0
    for i in rzuty_kostka:
        if i%2==0:
            licznik=0
            suma+=i
            continue
        if licznik%2==0:
            suma-=i
            licznik+=1
        else:
            drugi=random.randint(1,6)
            print(drugi)
            licznik = 0
            if drugi % 2 == 0:
                suma += drugi
                continue
            suma-=drugi


    return suma, suma>=cel


def rzucaj(ilosc_rzutow):
    wyniki_rzutow_kostka=[random.randint(1,6) for i in range(ilosc_rzutow)]
    return wyniki_rzutow_kostka


if __name__ == "__main__":
    main()