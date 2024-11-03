"""
PPiPD laby 1 zadanie nr 3
Laby Zadanie nr 1.3 py
"""
def main():
    dlugosc = int(input("podaj dlugosc budynku: "))
    szerokosc = int(input("podaj szerokosc budynku: "))
    wysokosc = int(input("podaj wysokosc budynku: "))
    if wysokosc<=0 or szerokosc<=0 or dlugosc<=0:
        raise ValueError("Bledne dane")
    pole_powierzchni = 2* ((dlugosc*wysokosc) + (szerokosc*wysokosc))
    ilosc_rolek = pole_powierzchni/2.548
    print(f"Potrzeba {ilosc_rolek}.")
    if ilosc_rolek<=400:
        koszt = 1.37 * ilosc_rolek
    else:
        koszt = 100 + (1.37 * ilosc_rolek)
    print (f"Papier będzie kosztował {koszt}zl.")
    return

if __name__ == '__main__':
        main()
