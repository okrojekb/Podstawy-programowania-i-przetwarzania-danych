'''
Zadanie punktowane"
'''

import math

def main():
    szerokosc = int(input("Podaj szerokosc prostokata: "))
    wysokosc = int(input("Podaj wysokosc prostokata: "))
    if wysokosc<=0 or szerokosc<=0:
        raise ValueError("Bledne dane")
    pocz_wspolrzedna_x = float(input("Podaj wspolrzedna x pilki: "))
    pocz_wspolrzedna_y = float(input("Podaj wspolrzedna y pilki: "))
    if pocz_wspolrzedna_x<0 or pocz_wspolrzedna_y<0:
        raise ValueError("Bledne dane")
    if pocz_wspolrzedna_x>szerokosc or pocz_wspolrzedna_y>wysokosc:
        raise ValueError("Bledne dane")
    pilka_predkosc_x = float(input("Podaj wspolrzedna x predkosci pilki: "))
    pilka_predkosc_y = float(input("Podaj wspolrzedna y predkosci pilki: "))
    if pilka_predkosc_x==0 and pilka_predkosc_y==0:
        raise ValueError("Bledne dane")
    czas_symulacji = float(input("Podaj czas symulacji: "))
    if czas_symulacji <0:
        raise ValueError("Bledne dane")
    x_wspolrzedna= pocz_wspolrzedna_x
    y_wspolrzedna = pocz_wspolrzedna_y
    calkowity_czas = 0
    czas_sprawdzania=1000000000000000000000000
    czas_etapu = 0
    while czas_symulacji>0:
        if pilka_predkosc_x>=0:
            docelowe_x=szerokosc
            czas_do_boku=(szerokosc-x_wspolrzedna)/pilka_predkosc_x
        else:
            docelowe_x = 0
            czas_do_boku = -(x_wspolrzedna / pilka_predkosc_x)
        if pilka_predkosc_y>=0:
            docelowe_y=wysokosc
            czas_do_gory=(wysokosc-y_wspolrzedna)/pilka_predkosc_y
        else:
            docelowe_y= 0
            czas_do_gory = -(y_wspolrzedna / pilka_predkosc_y)
        if czas_do_boku>czas_do_gory and (czas_symulacji-czas_do_gory)>=0:
            y_wspolrzedna=docelowe_y
            x_wspolrzedna+=(czas_do_gory*pilka_predkosc_x)
            czas_etapu=czas_do_gory
            czas_sprawdzania=czas_etapu
            pilka_predkosc_y=(-pilka_predkosc_y)
        elif czas_do_boku<czas_do_gory and (czas_symulacji-czas_do_gory)>=0:
            x_wspolrzedna=docelowe_x
            y_wspolrzedna+=(czas_do_boku*pilka_predkosc_y)
            czas_etapu=czas_do_boku
            czas_sprawdzania=czas_etapu
            pilka_predkosc_x=(-pilka_predkosc_x)
        elif  czas_do_boku==czas_do_gory and (czas_symulacji-czas_do_gory)>=0:
            y_wspolrzedna = docelowe_y
            x_wspolrzedna = docelowe_x
            czas_etapu = czas_do_gory
            czas_sprawdzania=czas_etapu
            pilka_predkosc_y = (-pilka_predkosc_y)
            pilka_predkosc_x = (-pilka_predkosc_x)
        if (czas_symulacji-czas_sprawdzania)>=0:
            calkowity_czas+=czas_etapu
            print(f"Pilka odbila sie w punkcie: ({x_wspolrzedna}, {y_wspolrzedna}) w czasie {calkowity_czas}.")
        czas_symulacji=czas_symulacji - czas_sprawdzania

    kon_wspol_x=x_wspolrzedna+((czas_symulacji+czas_sprawdzania)*pilka_predkosc_x)
    kon_wspol_y = y_wspolrzedna+((czas_symulacji+czas_sprawdzania)*pilka_predkosc_y)
    print(f"KOnczowe: {kon_wspol_x}, {kon_wspol_y}")

    for wiersz in range (wysokosc+1):
        for kolumna in range (szerokosc+1):
            if kolumna ==(wysokosc- int(kon_wspol_y)) and wiersz == (int(kon_wspol_x)):
                print("O", end="")
            elif kolumna == 0 or kolumna == szerokosc:
                print ("#", end="")
            elif wiersz==0 or wiersz == wysokosc:
                print("#", end="")
            else:
                print(" ", end="")

        print(" ")


    return



if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
