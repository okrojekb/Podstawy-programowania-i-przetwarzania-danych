"""
PPiPD laby 1 zadanie nr 3
Laby Zadanie nr 1.3 py
"""
def main():
    ilosc_col = int(input("podaj ilosc butelek coli, które chcesz zamówić: "))
    ilosc_pizza = int(input("podaj ilosc pizz hawajskich, ktore chcesz zamowic: "))
    if ilosc_pizza<0 or ilosc_col<0:
        raise ValueError("Bledne dane")

    if ilosc_pizza==0 and ilosc_col==0:
        print(f"Nie chcesz zamówić nic.")
        koszt = 0

    elif ilosc_pizza==0 or ilosc_col==0:
        print(f"Powinieneś zamówić {ilosc_col} butelek coli i {ilosc_pizza} pizz.")
        koszt = 5 + (ilosc_pizza*19.99) + (ilosc_col*6.99)
    else:
        if ilosc_pizza>=ilosc_col:
            zestawy= ilosc_col
            ilosc_pizza-=ilosc_col
            ilosc_col=0
            koszt = (ilosc_pizza * 19.99)+(zestawy * 25.99)


        else:
            zestawy = ilosc_pizza
            ilosc_col-=ilosc_pizza
            ilosc_pizza=0
            koszt = (zestawy*25.99) + (ilosc_col*6.99)
            print(f"Powinienes zamowic {zestawy} zestawow, {ilosc_pizza} pizz i {ilosc_col} butelek coli.")
    print(f"Koszt zamowienia wynosi: {koszt}zl.")


    return

if __name__ == '__main__':
        main()
