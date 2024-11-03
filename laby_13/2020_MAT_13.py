import copy

class Samolot:
    __slots__ = ["nazwa", "siedzenia", "wolne_miejsca"]
    def __init__(self, nazwa, liczba_rzedow, ile_miejsc_w_rzedzie):
        if liczba_rzedow<0 or ile_miejsc_w_rzedzie<0 or ile_miejsc_w_rzedzie>30:
            raise Exception
        self.nazwa = nazwa
        siedzenia=[None for i in range(liczba_rzedow)]
        for i in range(liczba_rzedow):
            siedzenia[i]=[0 for i in range(ile_miejsc_w_rzedzie)]
        self.siedzenia = siedzenia
        self.wolne_miejsca=liczba_rzedow*ile_miejsc_w_rzedzie

    def zamien_litere_na_liczbe(self, litera):
        return ord(litera.upper()) - ord('A')

    def zamien_liczbe_na_litere(self, liczba):
        return chr(liczba + ord('A'))

    def __repr__(self):
        #return f"Samolot (nazwa={self.nazwa}, liczba_rzedzow={len(self.siedzenia)}, ile_miejsc_w_rzedzie={len(self.siedzenia[0])})"
        return f"{self.siedzenia}, {self.wolne_miejsca}"


    def __str__(self):
        napis=""
        napis += f"{self.nazwa}\n"

        for i in range(len(self.siedzenia)+1):
            for j in range(len(self.siedzenia[0])+1):
                if i==0 and j==0:
                    napis+=f"{'':7s}"
                elif i==0:
                    numer_miejsca=self.zamien_liczbe_na_litere(j-1)
                    napis+=f"{numer_miejsca:5s}"
                elif j==0:
                    napis+=f"{i:3d}"
                else:
                    napis+= f"{self.sprawdz_czy_miejsce_wolne(i-1,j-1):5d}"
            napis+=f"\n"

        return napis



    def znajdz_numer(self, numer_miejsca):
        numer_wiersza=numer_miejsca[0]
        for i in range(1,len(numer_miejsca)-1):
            numer_wiersza+=numer_miejsca[i]
        numer_kolumny=numer_miejsca[len(numer_miejsca)-1]
        return numer_wiersza, numer_kolumny

    def sprawdz_czy_miejsce_wolne(self, w,k):
        if self.siedzenia[w][k]==0:
            return 0
        else:
            return 1

    def rezerwuj_miejsce(self, numer_miejsca):
        w, k = self.znajdz_numer(numer_miejsca)
        w=int(w) - 1
        k=self.zamien_litere_na_liczbe(k)
        if self.sprawdz_czy_miejsce_wolne(w, k)==0:
            self.siedzenia[w][k]=1
            self.wolne_miejsca-=1
            return True
        else:
            return False

    def liczba_wolnych_miejsc(self):
        return self.wolne_miejsca

    def skopiuj_samolot_z_rezerwacjami(self, nowa_nazwa):
        kopia=copy.deepcopy(self)
        kopia.nazwa=nowa_nazwa
        return kopia


    def __sub__(self, other):
        if type(other)!=type(self):
            raise Exception
        if len(self.siedzenia)!=len(other.siedzenia) or len(self.siedzenia[0])!=len(other.siedzenia[0]):
            raise Exception
        wynik=copy.copy(self)
        for i in range(len(self.siedzenia)):
            for j in range(len(self.siedzenia[0])):
                czy_wolne=self.sprawdz_czy_miejsce_wolne(i, j)
                if czy_wolne==1 and czy_wolne == self.sprawdz_czy_miejsce_wolne(i, j):
                    wynik.siedzenia[i][j]=0
        return wynik




def main():
    print('--------- ETAP 1 ----------')

    airbus = Samolot('Embraer 190', 5, 4)
    print(airbus)
    #print(airbus.__repr__())


    #print(airbus.znajdz_numer('3B'))

    print('--------- ETAP 2 ----------')

    print(f"Rezerwacja miejsca 1A zakończkona: {airbus.rezerwuj_miejsce('1A')}")
    #print(airbus)
    #print(airbus.__repr__())


    print(f"Rezerwacja miejsca 2b zakończkona: {airbus.rezerwuj_miejsce('2b')}")
    #print(airbus.__repr__())

    print(f"Rezerwacja miejsca 3C zakończkona: {airbus.rezerwuj_miejsce('3C')}")
    print(f"Rezerwacja miejsca 4D zakończkona: {airbus.rezerwuj_miejsce('4D')}")
    print(f"Rezerwacja miejsca 5C zakończkona: {airbus.rezerwuj_miejsce('5C')}")
    print(f"Rezerwacja miejsca 4B zakończkona: {airbus.rezerwuj_miejsce('4B')}")
    print(f"Rezerwacja miejsca 3A zakończkona: {airbus.rezerwuj_miejsce('3A')}")
    #print(f"Rezerwacja miejsca 3A zakończkona: {airbus.rezerwuj_miejsce('3A')}")
    #print(airbus.__repr__())
    print(airbus)

    #assert not airbus.sprawdz_czy_miejsce_wolne(3,0), 'Miejsce dopiero zostało zarezerwowane'
    #assert airbus.sprawdz_czy_miejsce_wolne(4, 2), 'Miejsce jeszcze nie zostało zarezerwowane'
    print()
    print(airbus)
    #print(airbus.__repr__())
    print('--------- ETAP 3 ----------')

    print(f'Ilość wolnych miejsc w samolocie to: {airbus.liczba_wolnych_miejsc()}')

    print('--------- ETAP 4 ----------')

    airbus_kopia = airbus.skopiuj_samolot_z_rezerwacjami('Embraer 190+')
    print(airbus_kopia)

    # orginalny obiekt nie powinien ulec zmianie
    print(f"Rezerwacja miejsca 1B zakończkona: {airbus_kopia.rezerwuj_miejsce('1B')}")
    print(f"Rezerwacja miejsca 1C zakończkona: {airbus_kopia.rezerwuj_miejsce('1C')}")
    print(f"Rezerwacja miejsca 1D zakończkona: {airbus_kopia.rezerwuj_miejsce('1D')}")
    #assert airbus.sprawdz_czy_miejsce_wolne(1, 1), "Kopia się nie udała"
    #assert airbus.sprawdz_czy_miejsce_wolne(1,2), "Kopia się nie udała"
    #assert airbus.sprawdz_czy_miejsce_wolne(1,3), "Kopia się nie udała"
    print(airbus)
    print(airbus_kopia)


    print("------------------------------------------------------------")

    latacz = Samolot("Spiulkolot", 13, 7)
    print(latacz)

    print('--------- ETAP 5 ----------')

    samolot_z_roznica = airbus_kopia - airbus
    print(samolot_z_roznica)

    samolot_z_roznica.rezerwuj_miejsce('5A')
    #assert airbus_kopia.sprawdz_czy_miejsce_wolne('5A'), "Nie powinno się zmienić miejsce oryginalne"

if __name__ == '__main__':
    main()