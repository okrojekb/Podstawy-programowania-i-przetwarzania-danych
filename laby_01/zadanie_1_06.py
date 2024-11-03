def main():
    liczba_na_dole = int(input("Podaj liczbe osob na dole: "))
    liczba_na_gorze = int(input("Podaj liczbe osob na gorze: "))
    if liczba_na_gorze<0 or liczba_na_dole<0:
        raise ValueError("Bledne dane")
    if liczba_na_gorze%8==0:
        ilosc_kursow_na_dol = liczba_na_gorze//8
    elif liczba_na_gorze%8!=0:
        ilosc_kurow_na_dol = (liczba_na_gorze//8)+1
    if liczba_na_dole%8==0:
        ilosc_kursow_na_gore = liczba_na_dole//8
    elif liczba_na_dole%8!=0:
        ilosc_kurow_na_gore = (liczba_na_dole//8)+1
    if ilosc_kursow_na_gore>ilosc_kurow_na_dol:
        suma_kursow = (ilosc_kursow_na_gore*2)-1
    elif ilosc_kurow_na_gore<=ilosc_kursow_na_dol:
        suma_kursow = (ilosc_kursow_na_dol*2)
    print(f"Winda musi wykonac {suma_kursow} kursow, zeby przewiesc wszystkich.")






if __name__ == '__main__':
    main()