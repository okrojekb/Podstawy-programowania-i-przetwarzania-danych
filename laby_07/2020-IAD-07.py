'''
laby nr 4
zadanie 1
'''

import random
import math
import copy


def wygeneruj_prosta_sciezke(n):
    """
    Zwraca n-elementową listę o wartościach [0,1,2,3,...,n-1]
    :param n: długość listy
    :return: lista
    """
    lista=[0]*n
    for i in range(n):
        lista[i]=i
    return lista


def wygeneruj_miasta_A(n, min_x=-10, max_x=10, min_y=-10, max_y=10):
    """
    Generuje dwie listy (jedna ma współrzędne x, a druga współrzędne y) reprezentujące współrzędne miast.
    Współrzędne miast są losowane z rozkładu jednostajnego U[min_x, max_x] dla współrzędnych x oraz U[min_y, max_y]
    dla współrzędnych y.
    :param n: liczba miast
    :param min_x: minimalna współrzędna x
    :param max_x: maksymalna współrzędna x
    :param min_y: minimalna współrzędna y
    :param max_y: maksymalna współrzędna y
    :return: dwuelementowa krotka, gdzie pierwszy element jest n-elementową listą współrzędnych x,
    a drugi element n-elementową listą współrzędnych y
    """
    wspol_x = [0]*n
    wspol_y = [0]*n
    for i in range(n):
        wspol_x[i]=random.uniform(min_x, max_x)
        wspol_y[i]=random.uniform(min_y, max_y)
    return wspol_x,wspol_y


def oblicz_dlugosc_sciezki_A(miasta_x, miasta_y, sciezka):
    """
    Dla zadanej listy indeksów miast oblicz długość cyklu. Wyjaśnijmy: pomimo nazwy parametru "sciezka" mamy na myśli
    cykl: z ostatniego miasta przechodzimy z powrotem do pierwszego (zerowego).
    :param miasta_x: lista współrzędnych x-owych miast
    :param miasta_y: lista współrzędnych y-owych miast
    :param sciezka: lista indeksów miast, zgodnie z którą przemieszczamy się od miasta do miasta. Z ostatniego miasta
    przechodzimy z powrotem do pierwszego (zerowego).
    :return: pojedyncza liczba typu float oznaczająca długość cyklu
    """
    dlugosc_cyklu = 0
    for i in range(len(sciezka)-1):
        indeks=sciezka[i]
        kolejny_indeks=sciezka[i+1]
        odleglosc=math.sqrt((miasta_x[indeks]-miasta_x[kolejny_indeks])**2 + (miasta_y[indeks]-miasta_y[kolejny_indeks])**2)
        dlugosc_cyklu+=odleglosc
    ost_indeks=sciezka[len(sciezka)-1]
    pier_indeks=sciezka[0]
    odleglosc_ost=math.sqrt((miasta_x[ost_indeks]-miasta_x[pier_indeks])**2 + (miasta_y[ost_indeks]-miasta_y[pier_indeks])**2)
    dlugosc_cyklu+=odleglosc_ost
    return dlugosc_cyklu


def mutuj_A(sciezka, k=3):
    """
    Funkcja mutuje podaną listę indeksów. Funkcja nie modyfikuje argumentów wejściowych. Funkcja zwraca zmodyfikowaną kopię.
    Funkcja działa w sposób następujący: losowane jest k indeksów listy bez zwracania. Następnie geny są przesuwane cyklicznie
    po wylosowanych indeksach. Przykładowo, jeśli lista to [1,11,2,3,22,4,5,33], a wylosowane indeksy to [1,4,7] (dwucyfrowe elementy
    z listy) to wynikowa ścieżka powinna być równa [1,22,2,3,33,4,5,11].

    Można (należy) użyć random.sample().

    :param sciezka: Lista indeksów, którą należy zmutować.
    :param k: Liczba indeksów do wylosowania (domyślnie równy 3)
    :return: Zmutowana kopia ścieżki
    """
    wynikowa_sciezka=copy.copy(sciezka)
    lista_indeksow=wygeneruj_prosta_sciezke(len(sciezka))
    wylosowane=[0]*k
    wylosowane=random.sample(lista_indeksow, k)
    pomoc = wynikowa_sciezka[wylosowane[0]]
    for i in range(k-1):
        indeks=wylosowane[i]
        kolejny_indeks=wylosowane[i+1]
        wynikowa_sciezka[indeks]=wynikowa_sciezka[kolejny_indeks]
    ost_indeks=wylosowane[k-1]
    wynikowa_sciezka[ost_indeks]=pomoc
    return wynikowa_sciezka


def krzyzuj_A(sciezka1, sciezka2):
    """
    Funkcja dokonuje krzyżowania dwóch ścieżek. Krzyżowanie polega na wylosowaniu pewnego indeksu z zakresu {1, 2,..., n-2}
    (gdzie n to długość jednej ścieżki), a następnie przepisanie elementów ze ścieżki 1 do dziecka od zera do wylosowanego indeksu.
    Reszta indeksów miast powinna zostać wpisana w pozostałe miejsca zgodnie z kolejnością występowania na sciezka2.

    Przykładowo, jeśli sciezka1=[0,1,2,3,4,5,6], a sciezka2=[6,5,4,3,2,1,0], a wylosowany index=3, to dziecko powinno mieć
    postać [0,1,2,6,5,4,3].

    :param sciezka1: lista indeksów miast
    :param sciezka2: lista indeksów miast
    :return: lista indeksów miast
    """
    n=len(sciezka1)
    indeks=random.randint(1,n-2)

    dziecko=[0]*n
    for i in range(indeks):
        dziecko[i]=sciezka1[i]
    licznik=0
    ilosc_powtorzen=0
    for j in range(indeks, len(dziecko)):
        while True:
            elem1=sciezka2[licznik]
            for k in range(indeks):
                elemdz=dziecko[k]
                ilosc_powtorzen=0
                if elem1==elemdz:
                    ilosc_powtorzen+=1
                    break
            licznik+=1
            if ilosc_powtorzen==0:
                break

        dziecko[j]=elem1



    return dziecko


def znajdz_rozwiazanie_optymalne_A(miasta_x, miasta_y):
    """
    Znajduje rozwiązanie optymalne problemu komiwojażera poprzez rozpatrzenie wszystkich permutacji miast.
    :param miasta_x: lista współrzędnych x-owych miast
    :param miasta_y: lista współrzędnych y-owych miast
    :return: krotka, której pierwszym elementem jest optymalna długość cyklu, a drugim optymalna lista indeksów miast
    """


    pass


def main_A():
    random.seed(123)
    n = 7
    min_x, max_x, min_y, max_y = -5, 4, -4, 5
    # grupa A
    # etap 1
    print("0. Generujemy miasta")
    miasta_x, miasta_y = wygeneruj_miasta_A(n, min_x, max_x, min_y, max_y)
    print(miasta_x)
    print(miasta_y)

    print("\n\n1. Szukamy prostą mutacją")
    sciezka = wygeneruj_prosta_sciezke(n)
    print(f"Prosta sciezka: {sciezka}")
    best_sciezka = sciezka
    best_wartosc = oblicz_dlugosc_sciezki_A(miasta_x, miasta_y, sciezka)
    print(f"Dla prostej ścieżki długość ścieżki to: {best_wartosc}")

    print(f"mutuj_A([0,1,2,3,4,5,6], 3) = {mutuj_A([0, 1, 2, 3, 4, 5, 6], 3)}")
    print(f"mutuj_A([0,1,2,3,4,5,6], 4) = {mutuj_A([0, 1, 2, 3, 4, 5, 6], 4)}")
    print(f"mutuj_A([0,1,2,3,4,5,6], 5) = {mutuj_A([0, 1, 2, 3, 4, 5, 6], 5)}")
    for i in range(100):
        zmutowana_sciezka=mutuj_A(best_sciezka)
        nowa_dlugosc=oblicz_dlugosc_sciezki_A(miasta_x,miasta_y,zmutowana_sciezka)
        if nowa_dlugosc<best_wartosc:
            best_wartosc=nowa_dlugosc
            best_sciezka=zmutowana_sciezka

    # [TO UZUPELNIJ]
    # 100 razy wykonaj:
    # mutację aktualnie najlepszej ścieżki
    # sprawdzenie, czy zmutowana ścieżka daje krótszy (lepszy) cykl
    # jeśli tak, zapisz lepszy wynik w zmiennych best_sciezka, best_wartosc

    print(f"Po mutacjach długość ścieżki {best_sciezka} to: {best_wartosc}")

    print("\n\n2. Szukamy przez krzyzowanie")

    sciezka1 = mutuj_A(wygeneruj_prosta_sciezke(n), n - 2)
    sciezka2 = mutuj_A(wygeneruj_prosta_sciezke(n), n - 2)
    wartosc1 = oblicz_dlugosc_sciezki_A(miasta_x, miasta_y, sciezka1)
    wartosc2 = oblicz_dlugosc_sciezki_A(miasta_x, miasta_y, sciezka2)
    #print(f"wartosc sciezki1 na p: {wartosc1}")
    #print(f"wartosc sciezki2 na p: {wartosc2}")
    if wartosc1>wartosc2:
        pomoc=sciezka1
        sciezka1=sciezka2
        sciezka2=pomoc
        pomoc=wartosc1
        wartosc1=wartosc2
        wartosc2=pomoc
        #print(f"wartosc sciezki1 na po zmianie: {wartosc1}")
        #print(f"wartosc sciezki2 na po zmianie: {wartosc2}")

    for i in range(1000):
        dziecko=krzyzuj_A(sciezka1, sciezka2)
        dlugosc_dziecka=oblicz_dlugosc_sciezki_A(miasta_x,miasta_y,dziecko)
        #print(f"wartosc dziecka na: {dlugosc_dziecka}")
        if wartosc1 <= dlugosc_dziecka <= wartosc2:
            sciezka2 = dziecko
            wartosc2 = dlugosc_dziecka
        elif dlugosc_dziecka <= wartosc1:
            sciezka2 = sciezka1
            wartosc2 = wartosc1
            sciezka1 = dziecko
            wartosc1 = dlugosc_dziecka
        '''
        if dlugosc_dziecka<wartosc2:
            sciezka1=sciezka2
            sciezka2=dziecko
            wartosc1=wartosc2
            wartosc2=dlugosc_dziecka
        else:
            if dlugosc_dziecka<wartosc1:
                sciezka1=dziecko
                wartosc1=dlugosc_dziecka
        #print(f"wartosc sciezki1 na: {wartosc1}")
        #print(f"wartosc sciezki2 na: {wartosc2}")
        '''
    # [TO UZUPELNIJ]
    # Nasza populacja składa się ze sciezka1 i sciezka2
    # Powtórz 1000 razy:
    # skrzyżuj ścieżkę1 i ścieżkę2
    # oblicz długość cyklu dla dziecka
    # pozostaw w zmiennych sciezka1, wartosc1 i sciezka2, wartosc2 wartosci odpowiadajace dwóm najlepszym wynikom z trzech możliwych (sciezka1, sciezka2, dziecko)
    # Podpowiedz: uzyj mechanizmu jak przy sortowaniu przez wstawianie.


    print(f"\n\nPo krzyżowaniu długość ścieżki {sciezka1} to: {wartosc1}")

    # etap 5:

    optymalne = znajdz_rozwiazanie_optymalne_A(miasta_x, miasta_y)
    print(f"\n\n3. Optymalny wynik to {optymalne}")


if __name__ == "__main__":
    main_A()