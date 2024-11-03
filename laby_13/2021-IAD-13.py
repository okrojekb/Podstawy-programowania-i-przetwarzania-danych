import copy


class Zamowienie:
    __slots__ = ["towary", "ceny"]

    def __init__(self,lista=[]):
        towary=[]
        if lista==[]:
            self.towary=copy.copy(towary)
        else:
            towary=[0 for i in range(21)]
            if not type(lista)==list:
                raise ValueError("Musisz podać liste")
            for i in lista:
                indeks_towaru=i[0]
                liczba_sztuk=i[1]
                if type(indeks_towaru)!=int or type(indeks_towaru)!=int:
                    raise ValueError("Wartosci musza byc liczbami calkowitymi")
                if indeks_towaru>20 or indeks_towaru<0:
                    raise ValueError("Indeks towaru musi być w zakresie [0, 20]")
                if liczba_sztuk<=0:
                    raise ValueError("Liczba sztuk musi być dodatnia")
                towary[indeks_towaru]=liczba_sztuk
            while towary[len(towary)-1]==0:
                towary.pop()
            self.towary=copy.copy(towary)
            self.ceny=[i + 1 for i in range(21)]


    def __repr__(self):
        return f"Zamówienie(towary = {self.towary})"

    def __str__(self):
        napis="towar:   "
        for i in range(len(self.towary)):
            napis+=f"{i:3d}"
        napis+="\n"
        napis+="sztuk:   "
        for i in self.towary:
            napis+=f"{i:3d}"
        return napis

    def oblicz_wartosc(self):
        suma=0
        for i in range(len(self.towary)):
            if self.towary[i]==0:
                continue
            suma+=self.towary[i] * self.ceny[i]
        return suma

    def __lt__(self, other):
        if type(other)!=type(self):
            raise ValueError("Musisz podać dwie instancje klasy Zamowienie")
        cena1=self.oblicz_wartosc()
        cena2=other.oblicz_wartosc()
        return cena1<cena2

    def __add__(self, other):
        towary=copy.copy(self.towary)
        if type(other)==tuple and type(other[0])==int and type(other[1])==int:
            while other[0]>len(towary):
                towary.append(0)
            if other[0]==len(towary):
                towary.append(other[1])
            else:
                towary[other[0]]+=other[1]
        elif type(other)==type(self):
            dlugosc=max(len(self.towary), len(other.towary))
            towary=[0 for i in range(dlugosc)]
            for i in range(dlugosc):
                if len(self.towary)<=i:
                    towary[i] = other.towary[i]
                elif len(other.towary)<=i:
                    towary[i] = self.towary[i]
                else:
                    towary[i]=self.towary[i] + other.towary[i]
        else:
            raise ValueError("nie można dodac takiego typu")
        lista=[]
        for i in range(len(towary)):
            if towary[i]==0:
                continue
            lista.append([i,towary[i]])
        return Zamowienie(lista)

    def __iadd__(self, other):
        if type(other) == tuple and type(other[0]) == int and type(other[1]) == int:
            while other[0] > len(self.towary):
                self.towary.append(0)
            if other[0] == len(self.towary):
                self.towary.append(other[1])
            else:
                self.towary[other[0]] += other[1]
        elif type(other) == type(self):
            dlugosc = max(len(self.towary), len(other.towary))
            towary = [0 for i in range(dlugosc)]
            for i in range(dlugosc):
                if len(self.towary) <= i:
                    towary[i] = other.towary[i]
                elif len(other.towary) <= i:
                    towary[i] = self.towary[i]
                else:
                    towary[i] = self.towary[i] + other.towary[i]
            self.towary=towary
        else:
            raise ValueError("nie można dodac takiego typu")
        return self




def main():

    ##################### ETAP1 #####################
    print("## ETAP1: STWORZENIE KLASY, KONSTRUKTOR (2 PUNKTY) ##")
    zamowienie1 = Zamowienie([(1, 9), (3, 5), (4, 2), (7, 4), (0, 1)])
    zamowienie2 = Zamowienie([(0, 5), (4, 7), (19, 8), (7, 1)])
    zamowienie3 = Zamowienie()
    print(zamowienie1.towary)
    print(zamowienie2.towary)
    print(zamowienie3.towary)


    ##################### ETAP2 #####################
    print("\n## ETAP2: WYPISYWANIE (1 PUNKT) ##")
    print(zamowienie1.__repr__())
    print(zamowienie1.__str__())


    ##################### ETAP3 #####################
    print("\n## ETAP3: OBLICZANIE CENY, PORÓWNYWANIE (2 PUNKTY) ##")
    print(f"Ceny: {zamowienie1.ceny}")
    print(f"zamowienie1:\n{zamowienie1}")
    print(f"Cena zamowienie1: {zamowienie1.oblicz_wartosc()}")
    print(f"zamowienie2:\n{zamowienie2}")
    print(f"Cena zamowienie2: {zamowienie2.oblicz_wartosc()}")
    print(f"zamowienie1 < zamowienie2: {zamowienie1 < zamowienie2}")


    ##################### ETAP4 #####################
    print("\n## ETAP4: DODAWANIE ##")
    print("## Zamowienie + Zamowienie (2 PUNKTY) ##\n")
    print("zamowienie3 = zamowienie1 + zamowienie2")
    zamowienie3 = zamowienie1 + zamowienie2
    print(f"zamowienie1:\n{zamowienie1}")
    print(f"zamowienie2:\n{zamowienie2}")
    print(f"zamowienie3:\n{zamowienie3}")
    #
    print("\n## Zamowienie + tuple (2 PUNKTY) ##\n")
    print("zamowienie4 = zamowienie1 + (0, 3)")
    zamowienie4 = zamowienie1 + (0, 3)
    print(f"zamowienie1:\n{zamowienie1}")
    print(f"zamowienie4:\n{zamowienie4}")

    print("\nzamowienie5 = zamowienie1 + (17, 5)")
    zamowienie5 = zamowienie1 + (17, 5)
    print(f"zamowienie1:\n{zamowienie1}")
    print(f"zamowienie5:\n{zamowienie5}")
    #
    print("\n## += (1 PUNKT) ## \n")
    print("zamowienie1 += Zamowienie([(9, 3), (2, 5)])")
    zamowienie1 += Zamowienie([(9, 3), (2, 5)])
    print(f"zamowienie1:\n{zamowienie1}")
    #
    print("\nzamowienie1 += (5, 9)")
    zamowienie1 += (5, 9)
    print(f"zamowienie1:\n{zamowienie1}")




if __name__ == "__main__":
    main()