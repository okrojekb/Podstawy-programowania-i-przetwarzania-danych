"""
Przykładowe rozwiązanie zadania 2020-MAT-13
"""
import copy

class Samolot:
    """ Definicja klasy Samolot """
    __slots__ = ["nazwa", "siedzenia", "liczba_wolnych_miejsc"]

    def __init__(self, nazwa, liczba_rzedow, ile_miejsc_w_rzedzie):
        """ Definicja konstruktora klasy """
        if liczba_rzedow <= 0 or ile_miejsc_w_rzedzie <= 0:
            raise ValueError("Liczby miejsc i rzedow musza byc dodatnie.")

        self.nazwa = nazwa
        self.siedzenia = [ [0] * ile_miejsc_w_rzedzie for i in range(liczba_rzedow) ]
        self.liczba_wolnych_miejsc = liczba_rzedow * ile_miejsc_w_rzedzie

    # Metody pomocnicze:
    def zamien_liczbe_na_litere(self, liczba):
        return chr(liczba + ord('A'))

    def zamien_litere_na_liczbe(self, litera):
        return ord(litera.upper()) - ord('A')

    def __repr__(self):
        """ techniczna reprezentacj """
        return f"Samolot({self.nazwa}, {len(self.siedzenia)}, {len(self.siedzenia[0])})"

    def __str__(self):
        """ ładna reprezentacja """
        repr = f"{self.nazwa}\n    "

        for miejsce in range( len(self.siedzenia[0]) ):
            repr += self.zamien_liczbe_na_litere(miejsce)
        repr += '\n'

        # wypisanie zawartosci macierzy:
        for rzad in range( len(self.siedzenia) ):
            repr += f"{rzad + 1}   " # dodajemy numery rzedow
            for miejsce in range( len(self.siedzenia[0]) ):
                repr += f"{self.siedzenia[rzad][miejsce]}"
            repr += "\n"

        return repr

    def rozszyfruj_numer_miejsca(self, numer_miejsca):
        """
        Metoda zamienia numer_miejsca postaci
        '3B' na dwie liczby calkowite:
        2 == 3-1 -> numer rzedu (wiersza)
        1 == B -> numer kolumny
        """
        # odwolujemy sie do ostatniego elementu napisu
        miejsce = numer_miejsca[len(numer_miejsca) - 1]
        miejsce = self.zamien_litere_na_liczbe(miejsce) # zamieniamy na liczbe

        rzad = ""
        for i in range(len(numer_miejsca)-1):
            rzad += numer_miejsca[i]
        rzad = int(rzad) - 1
        # pomijamy sprawdzanie warunkow poprawnosci

        return [rzad, miejsce]

    def sprawdz_czy_miejsce_wolne(self, numer_miejsca):
        """ sprawdzamy czy miejsce jest wolne """
        rzad, miejsce = self.rozszyfruj_numer_miejsca(numer_miejsca)
        return self.siedzenia[rzad][miejsce] == 0

    def rezerwuj_miejsce(self, numer_miejsca):
        """ rezerwujemy miejsce jesli to mozliwe """
        rzad, miejsce = self.rozszyfruj_numer_miejsca(numer_miejsca)

        if self.sprawdz_czy_miejsce_wolne(numer_miejsca):
            self.siedzenia[rzad][miejsce] = 1
            self.liczba_wolnych_miejsc -= 1
            return True

        return False
    def ile_wolnych_miejsc(self):
        return self.liczba_wolnych_miejsc

    def skopiuj_samolot_z_rezerwacjami(self, nazwa):
        kopia = Samolot(nazwa, len(self.siedzenia), len(self.siedzenia[0]))

        kopia.siedzenia = copy.deepcopy(self.siedzenia)

        # for rzad in range(len(self.siedzenia)):
        #     for miejsce in range(len(self.siedzenia[0])):
        #         kopia.siedzenia[rzad][miejsce] = self.siedzenia[rzad][miejsce]

        kopia.liczba_wolnych_miejsc = self.liczba_wolnych_miejsc
        return kopia

    def __sub__(self, other):
        """
        Odejmowanie samolotów
        W wyniku dostaniemy nowy samolot, który będzie miał zarezerwowane takie siedzenia, że:
        * są one zarezerwowane w samolocie self
        * nie są zarezerowowane w samolocie other
        """

        # Sprawdzamy czy rozmiary samolotów są takie same
        if len(self.siedzenia) != len(other.siedzenia) or len(self.siedzenia[0]) != len(other.siedzenia[0]):
            raise ValueError()
        # Torzymy wynikowy samolot:
        wynik = Samolot(self.nazwa,
                        len(self.siedzenia),
                        len(self.siedzenia[0]))

        # Odpowiednio uzupełniamy rezerwacje:
        for rzad in range(len(self.siedzenia)):
            for miejsce in range(len(self.siedzenia[0])):

                if self.siedzenia[rzad][miejsce] == 1 and other.siedzenia[rzad][miejsce] == 0:
                    wynik.siedzenia[rzad][miejsce] = 1
                    wynik.liczba_wolnych_miejsc -= 1

        return wynik


def main():
    # Przyklad:
    # s = Samolot("Boeing", 3, 3)
    # print(s)
    # print(s.nazwa)
    # print(s.siedzenia)

    print('--------- ETAP 1 ----------')

    airbus = Samolot('Embraer 190', 5, 4)
    print(airbus)

    print('--------- ETAP 2 ----------')

    print(f"Rezerwacja miejsca 1A zakończkona: {airbus.rezerwuj_miejsce('1A')}")
    print(f"Rezerwacja miejsca 2b zakończkona: {airbus.rezerwuj_miejsce('2b')}")
    print(f"Rezerwacja miejsca 3C zakończkona: {airbus.rezerwuj_miejsce('3C')}")
    print(f"Rezerwacja miejsca 4D zakończkona: {airbus.rezerwuj_miejsce('4D')}")
    print(f"Rezerwacja miejsca 5C zakończkona: {airbus.rezerwuj_miejsce('5C')}")
    print(f"Rezerwacja miejsca 4B zakończkona: {airbus.rezerwuj_miejsce('4B')}")
    print(f"Rezerwacja miejsca 3A zakończkona: {airbus.rezerwuj_miejsce('3A')}")
    print(f"Rezerwacja miejsca 3A zakończkona: {airbus.rezerwuj_miejsce('3A')}")
    assert not airbus.sprawdz_czy_miejsce_wolne('3A'), 'Miejsce dopiero zostało zarezerwowane'
    assert airbus.sprawdz_czy_miejsce_wolne('4C'), 'Miejsce jeszcze nie zostało zarezerwowane'
    print()
    print(airbus)

    print('--------- ETAP 3 ----------')

    print(f'Ilość wolnych miejsc w samolocie to: {airbus.ile_wolnych_miejsc()}')

    print('--------- ETAP 4 ----------')

    airbus_kopia = Samolot.skopiuj_samolot_z_rezerwacjami(airbus, 'Embraer 190+')
    print(airbus_kopia)

    # orginalny obiekt nie powinien ulec zmianie
    print(f"Rezerwacja miejsca 1B zakończkona: {airbus_kopia.rezerwuj_miejsce('1B')}")
    print(f"Rezerwacja miejsca 1C zakończkona: {airbus_kopia.rezerwuj_miejsce('1C')}")
    print(f"Rezerwacja miejsca 1D zakończkona: {airbus_kopia.rezerwuj_miejsce('1D')}")
    assert airbus.sprawdz_czy_miejsce_wolne('1B'), "Kopia się nie udała"
    assert airbus.sprawdz_czy_miejsce_wolne('1C'), "Kopia się nie udała"
    assert airbus.sprawdz_czy_miejsce_wolne('1D'), "Kopia się nie udała"
    print(airbus)
    print(airbus_kopia)

    print('--------- ETAP 5 ----------')

    samolot_z_roznica = airbus_kopia - airbus
    print(samolot_z_roznica)

    samolot_z_roznica.rezerwuj_miejsce('5A')
    assert airbus_kopia.sprawdz_czy_miejsce_wolne('5A'), "Nie powinno się zmienić miejsce oryginalne"

if __name__ == "__main__":
    main()