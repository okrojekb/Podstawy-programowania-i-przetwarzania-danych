"""
PPiPD laby 1 zadanie nr 3
Laby Zadanie nr 1.3 py
"""
def main():
   waga = float(input("Podaj swoja wage (jako calkowita liczbe kg): "))
   if waga!=int(waga):
       raise ValueError("Podana waga musi być liczba calkowita.")
   if waga<0:
       raise ValueError("Waga musi byc liczba nieujemna.")
   waga=int(waga)
   wzrost = float(input("Podaj swoj wzrost (jako calkowita liczbe cm): "))
   if wzrost!=int(wzrost):
       raise ValueError("Podany wzrost musi być liczba calkowita.")
   if wzrost<0:
       raise ValueError("Wzrost musi byc liczba nieujemna.")
   wzrost=wzrost/100
   BMI = Liczenie_BMI(waga, wzrost)
   stan_wagi = Sprawdzenie_stanu(BMI)
   print(f"Twoje BMI to: {BMI}. Oznacza to, ze masz {stan_wagi}.")
   return

def Liczenie_BMI(waga, wzrost):
    kwadrat_wzrostu = wzrost*wzrost
    BMI = waga/kwadrat_wzrostu
    return BMI

def Sprawdzenie_stanu (BMI):
    if BMI<=18.5:
        wynik = "niedowage"
    elif BMI<=25:
        wynik = "wage prawidlowa"
    elif BMI<=30:
        wynik = "nadwage"
    else:
        wynik = "otylosc"
    return wynik

if __name__ == '__main__':
        main()
