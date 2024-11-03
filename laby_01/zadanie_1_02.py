"""
PPiPD laby 1 zadanie nr 2
Laby Zadanie nr 1.2 py
"""
def main():
    waga = float(input("Podaj swoja wage w kilogramach: "))
    if waga <=0:
        raise ValueError("Waga musi być liczbą dodatnią.")
    liczba_porcji = int(input("Podaj liczbę wypitych porcji: "))
    #sprawdzic czy jest calkowite
    if liczba_porcji<0:
        raise ValueError("Liczba wypitych porcji musi być liczbą nieujemna.")
    wielkosc_porcji = int(input("Podaj wielkosc porcji (w ml): "))
    #sprawdzic czy jest calkowita
    if wielkosc_porcji<0:
        raise ValueError("Wielkosc porcji musi być liczbą nieujemna.")
    zawartosc_procentowa = float(input("Podaj zawartosc alkoholu w trunku (w postaci liczby calkowitej: "))
    if zawartosc_procentowa<0:
        raise ValueError("Zawartosc alkoholu w trunku musi być liczbą nieujemna.")
    if zawartosc_procentowa != int(zawartosc_procentowa):
        raise ValueError("Zawartosc alkoholu w trunku musi być liczbą calkowita.")
    plec = input("Wybierz plec ('kobieta' lub 'mężczyzna'): ")
    if plec!="kobieta" and plec!="mężczyzna":
        raise ValueError("Musisz wybrac plec wpisujac ('kobieta' lub 'mężczyzna'.")
    promile = ilosc_promili(liczba_porcji, wielkosc_porcji, zawartosc_procentowa, waga, plec)
    stan = sprawdz_stan(promile)
    print(f"Masz {promile} alkoholu we krwi. Jesteś {stan}.")
    return

def wypita_ilosc_czystego_alkoholu(liczba_porcji, wielkosc_porcji, zawartosc_procentowa):
    ulamek_alkoholu= zawartosc_procentowa/100
    wynik_ml = liczba_porcji*wielkosc_porcji*ulamek_alkoholu
    wynik_g = (wynik_ml*10)/12.5
    return wynik_g

def plec_a_wspolczynnik (plec):
    if plec=="kobieta":
        wynik = 0.6
    elif plec=="mężczyzna":
        wynik = 0.7
    return wynik

def ilosc_promili (liczba_porcji, wielkosc_porcji, zawartosc_procentowa, waga, plec):
    wspolczynnik_plci = plec_a_wspolczynnik(plec)
    wypity_czysty_alkohol_gramy = wypita_ilosc_czystego_alkoholu(liczba_porcji, wielkosc_porcji, zawartosc_procentowa)
    promile=(wypity_czysty_alkohol_gramy)/(wspolczynnik_plci*waga)
    return promile

def sprawdz_stan (ilosc_promili):
    if ilosc_promili<=0.2:
        stan = "trzeżwy"
    elif ilosc_promili>=5:
        stan = "w stanie zagrożenia życia"
    else:
        stan = "niezdolny do prowadzenia pojazdów mechanicznych"
    return stan

if __name__ == '__main__':
        main()
