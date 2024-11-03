import random
import math
import copy

def wygeneruj_prosta_sciezke(n):
    """
    Zwraca n-elementową listę [0,1,2,3,...,n-1]
    :param n: długość listy
    :return: lista
    """
    sciezka = [None] * n
    for i in range(n):
        sciezka[i] = i
    # sciezka = [i for i in range(n)]
    return sciezka


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
    miasta_x = [None] * n
    miasta_y = [None] * n
    for i in range(n):
        miasta_x[i] = random.uniform(min_x, max_x)
        miasta_y[i] = random.uniform(min_y, max_y)

    # miasta_x = [random.uniform(min_x, max_x) for _ in range(n)]
    # miasta_y = [random.uniform(min_y, max_y) for _ in range(n)]

    return miasta_x, miasta_y


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
    n = len(sciezka)
    dl = 0
    for i in range(1, n):
        dl += math.sqrt((miasta_x[sciezka[i - 1]] - miasta_x[sciezka[i]]) ** 2 + (
                miasta_y[sciezka[i - 1]] - miasta_y[sciezka[i]]) ** 2)
    dl += math.sqrt(
        (miasta_x[sciezka[n - 1]] - miasta_x[sciezka[0]]) ** 2 + (miasta_y[sciezka[n - 1]] - miasta_y[sciezka[0]]) ** 2)

    # lub:
    # for i in range(n):
    #     dl += math.sqrt((miasta_x[sciezka[i]] - miasta_x[sciezka[(i+1) % n]]) ** 2 + (miasta_y[sciezka[i]] - miasta_y[sciezka[(i+1)%n]]) ** 2)

    return dl


def znajdz_rozwiazanie_optymalne_A(miasta_x, miasta_y):
    """
    Znajduje rozwiązanie optymalne problemu komiwojażera poprzez rozpatrzenie wszystkich permutacji miast.
    :param miasta_x: lista współrzędnych x-owych miast
    :param miasta_y: lista współrzędnych y-owych miast
    :return: krotka, której pierwszym elementem jest optymalna długość cyklu, a drugim optymalna lista indeksów miast
    """
    n = len(miasta_x)
    sciezka = wygeneruj_prosta_sciezke(n)
    c = [None] * n
    for i in range(n):
        c[i] = 0
    # c = [0 for i in range(n)]

    optymalna_dlugosc = oblicz_dlugosc_sciezki_A(miasta_x, miasta_y, sciezka)
    optymalna_sciezka = sciezka

    # ktore = 0  # for debugging purposes only

    i = 0
    while i < n:
        if c[i] < i:
            if i % 2 == 0:
                sciezka[0], sciezka[i] = sciezka[i], sciezka[0]
            else:
                sciezka[c[i]], sciezka[i] = sciezka[i], sciezka[c[i]]
            # ktore += 1  # for debugging purposes only
            # print(f"{ktore}. {sciezka}")  # for debugging purposes only
            dlugosc = oblicz_dlugosc_sciezki_A(miasta_x, miasta_y, sciezka)
            if dlugosc < optymalna_dlugosc:
                optymalna_dlugosc = dlugosc
                optymalna_sciezka = sciezka
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1
    return optymalna_dlugosc, optymalna_sciezka


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
    sciezka_zmutowana = copy.copy(sciezka)
    n = len(sciezka)
    indeksy = random.sample([i for i in range(n)], k=k)
    wartosc_akt = sciezka_zmutowana[indeksy[0]]

    for i in range(k - 1):
        sciezka_zmutowana[indeksy[i]] = sciezka_zmutowana[indeksy[i + 1]]
    sciezka_zmutowana[indeksy[k - 1]] = wartosc_akt
    return sciezka_zmutowana


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
    n = len(sciezka1)
    index = random.randint(1, n - 2)
    # w drugiej grupie bedziemy jeszcze odwaracac kolejnosc
    dziecko = [None] * n
    for i in range(index):
        dziecko[i] = sciezka1[i]
    index_dziecko = index
    # dodaj reszte elementow z sciezki2, tylko te, ktorych jeszcze nie bylo,
    # w kolejnosci jak na sciezka2
    for i in range(n):
        el = sciezka2[i]
        czy_juz_jest = False
        for j in range(index):
            if dziecko[j] == el:
                czy_juz_jest = True
        if not czy_juz_jest:
            dziecko[index_dziecko] = sciezka2[i]
            index_dziecko += 1
    return dziecko


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

    # 100 razy wykonaj:
    # mutację aktualnie najlepszej ścieżki
    # sprawdzenie, czy zmutowana ścieżka daje krótszy (lepszy) cykl
    # jeśli tak, zapisz lepszy wynik w zmiennych best_sciezka, best_wartosc
    for i in range(100):
        sciezka_zmutowana = mutuj_A(best_sciezka, 3)
        wartosc = oblicz_dlugosc_sciezki_A(miasta_x, miasta_y, sciezka_zmutowana)
        if wartosc < best_wartosc:
            best_sciezka = sciezka_zmutowana
            best_wartosc = wartosc
    print(f"Po mutacjach długość ścieżki {best_sciezka} to: {best_wartosc}")

    print("\n\n2. Szukamy przez krzyzowanie")

    sciezka1 = mutuj_A(wygeneruj_prosta_sciezke(n), n - 2)
    sciezka2 = mutuj_A(wygeneruj_prosta_sciezke(n), n - 2)
    wartosc1 = oblicz_dlugosc_sciezki_A(miasta_x, miasta_y, sciezka1)
    wartosc2 = oblicz_dlugosc_sciezki_A(miasta_x, miasta_y, sciezka2)

    # zapewniamy, ze wartosc1 <= wartosc2
    # dzieki temu bedzie mozna trzymac 2 najlepsze wartosci z 3 przy idei sortowania przez wstawianie
    if wartosc1 > wartosc2:
        sciezka1, sciezka2 = sciezka2, sciezka1
        wartosc1, wartosc2 = wartosc2, wartosc1

    # Nasza populacja składa się ze sciezka1 i sciezka2
    # Powtórz 1000 razy:
    # skrzyżuj ścieżkę1 i ścieżkę2
    # oblicz długość cyklu dla dziecka
    # pozostaw w zmiennych sciezka1, wartosc1 i sciezka2, wartosc2 wartosci odpowiadajace dwóm najlepszym wynikom z trzech możliwych (sciezka1, sciezka2, dziecko)
    # Podpowiedz: uzyj mechanizmu jak przy sortowaniu przez wstawianie.
    for i in range(1000):
        dziecko = krzyzuj_A(sciezka1, sciezka2)
        wartosc_dziecko = oblicz_dlugosc_sciezki_A(miasta_x, miasta_y, dziecko)
        # print(dziecko)
        # print(wartosc_dziecko)
        if wartosc1 <= wartosc_dziecko <= wartosc2:
            sciezka2 = dziecko
            wartosc2 = wartosc_dziecko
        elif wartosc_dziecko <= wartosc1:
            sciezka2 = sciezka1
            wartosc2 = wartosc1
            sciezka1 = dziecko
            wartosc1 = wartosc_dziecko

    print(f"\n\nPo krzyżowaniu długość ścieżki {sciezka1} to: {wartosc1}")

    # etap 5:

    optymalne = znajdz_rozwiazanie_optymalne_A(miasta_x, miasta_y)
    print(f"\n\n3. Optymalny wynik to {optymalne}")


if __name__ == "__main__":
    main_A()
