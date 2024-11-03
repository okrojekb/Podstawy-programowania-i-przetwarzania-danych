"""
PPiPD laby 1 zadanie nr 3
Laby Zadanie nr 1.3 py
"""
def main():
    gotowka = int(input("podaj ilosc posiadanej gotowki: "))
    do_domu = int(input("podaj odleglosc do domu: "))
    if gotowka<0 or do_domu<0:
        raise ValueError("Bledne dane")
    if gotowka < 12.5:
        przejechane = 0
    elif gotowka <=60:
        gotowka -=10
        przejechane = gotowka/2.5
    else:
        gotowka -= 60
        przejechane = 20 + (gotowka/5)
    print(f"Mozesz pokonac {przejechane}km.")
    if do_domu>przejechane:
        wynik = "Nie uda"
    else:
        wynik = "Uda"
    print(f"{wynik} Ci sie dojechac do domu.")
    return



if __name__ == '__main__':
        main()
