'''
cwiczenia zestaw nr 3
'''

import math
import random
import copy


class Ulamek:
    __slots__ = ["licznik", "mianownik"]

    def __init__(self, licznik, mianownik):
        self.licznik = licznik
        self.mianownik = mianownik

    #def __repr__(self):
        #return f"Ulamek (licznik={self.licznik}, mianownik={self.mianownik})"

    def __repr__(self):
        return f"Ulamek wynosi: {self.licznik}/{self.mianownik}"

    def __add__(self, other):
        wynik = copy.copy(self)
        wynik.licznik = other.mianownik * wynik.licznik
        wynik.licznik+= (other.licznik * wynik.mianownik)
        wynik.mianownik *= other.mianownik
        return wynik

def main():
    a=Ulamek(1,2)
    b=Ulamek(1,4)
    print((a+b))


if __name__ == '__main__':
    main()