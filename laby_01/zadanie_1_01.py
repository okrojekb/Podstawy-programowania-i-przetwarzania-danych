"""
PPiPD zajęcia pierwsze
Zadanie testowe plik py
"""

def main():
    pokonane_schody = int(input("Podaj liczbe schodow, ktore pokonales "))
    if pokonane_schody>300 or pokonane_schody<0:
        raise Exception ("Bledne dane")
    numer_pietra = pokonane_schody//15
    if pokonane_schody%15==0:
        print (f"Jestes na {numer_pietra} pietrze")
        if numer_pietra%2==0:
            print("Masz 0 schodkow do toalety")
        else:
            print("Musisz pokonac 15 schodkow w gore albo w dol do najblizszej toalety")
    else:
        print (f"Jestes pomiedzy {numer_pietra}, a {numer_pietra+1} pietrem")
        if pokonane_schody%30<15:
            kierunek = "dol"
            ilosc_schodkow_do_lazienki=pokonane_schody%30
        else:
            kierunek = "gore"
            ilosc_schodkow_do_lazienki = 30-(pokonane_schody % 30)
        print(f"Musisz pokonac {ilosc_schodkow_do_lazienki} schodkow w {kierunek} do najblizszej toalety")


if __name__ =='__main__':
    main()
