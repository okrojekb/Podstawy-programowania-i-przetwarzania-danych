'''
laby nr 4
zadanie 1
'''
import random

def main():
    random.seed(2020)
    pozycja_1=0
    pozycja_2=0
    licznik=0
    while pozycja_1<20 and pozycja_2<20:
        print(f"Ruch kozicy {(licznik%2)+1}.")
        licznik+=1
        print("Co chcesz zrobic?")
        print("1 - skok")
        print("2 - mega skok")
        print("3 - atak")
        decyzja=int(input())
        if (licznik%2)==1:
            if decyzja==1:
                wynik=skok(pozycja_1)
                pozycja_1=wynik
            elif decyzja==2:
                wynik = mega_skok(pozycja_1)
                pozycja_1 = wynik
            elif decyzja==3:
                wynik = atak(pozycja_1, pozycja_2)
                pozycja_1 = wynik[0]
                pozycja_2 = wynik[1]
            else:
                raise ValueError("Bledne dane")
        else:
            if decyzja==1:
                wynik=skok(pozycja_2)
                pozycja_2=wynik
            elif decyzja==2:
                wynik = mega_skok(pozycja_2)
                pozycja_2 = wynik
            elif decyzja==3:
                wynik = atak(pozycja_2, pozycja_1)
                pozycja_2 = wynik[0]
                pozycja_1 = wynik[1]
            else:
                raise ValueError("Bledne dane")
        print(f"pozycja kozicy 1: {pozycja_1}")
        print(f"pozycja kozicy 2: {pozycja_2}")
    if pozycja_1>pozycja_2:
        print("WYGRYWA kozica 1!")
    elif pozycja_2>pozycja_1:
        print("WYGRYWA kozica 2!")
    elif pozycja_2==pozycja_1:
        print("REMIS")1

    return

def skok(pozycja_wykonujacego_ruch):
    numer=random.random()
    if numer<0.5:
        pozycja_wykonujacego_ruch+=1
        dlugosc_skoku= 1
    elif numer<0.8:
        pozycja_wykonujacego_ruch+=2
        dlugosc_skoku=2
    else:
        pozycja_wykonujacego_ruch+=3
        dlugosc_skoku=3
    print(f"Dlugosc skoku: {dlugosc_skoku}")
    return pozycja_wykonujacego_ruch

def mega_skok(pozycja_wykonujacego_ruch):
    numer=random.random()
    if numer<0.3:
        pozycja_wykonujacego_ruch+=5
        print("Kozica wykonala mega skok.")
    else:
        if pozycja_wykonujacego_ruch!=0:
            pozycja_wykonujacego_ruch-=1
            print("Mega skok sie nie udal, kozica cofa sie o 1 pole.")
        else:
            print("Mega skok sie nie udal.")

    return pozycja_wykonujacego_ruch

def atak(pozycja_wykonujacego_ruch, pozycja_nieaktywnego_gracza):
    if pozycja_wykonujacego_ruch<=pozycja_nieaktywnego_gracza:
        print("Strata ruchu, kozica, ktora jest nizej nie moze atakowac!")
        return pozycja_wykonujacego_ruch,pozycja_nieaktywnego_gracza
    numer=random.random()
    if numer>=0.5:
        pozycja_wykonujacego_ruch-=1
        print("Atak sie nie udal, atakujaca kozica cofa sie o 1 pole.")
    else:
        spadek=int(((pozycja_wykonujacego_ruch-pozycja_nieaktywnego_gracza)/2)**2)
        if pozycja_nieaktywnego_gracza<=spadek:
            spadek=pozycja_nieaktywnego_gracza
            pozycja_nieaktywnego_gracza=0
        else:
            pozycja_nieaktywnego_gracza-=spadek
        print(f"Atak sie powiodl, atakowana kozica cofa sie o {spadek} pola")
    return pozycja_wykonujacego_ruch,pozycja_nieaktywnego_gracza

if __name__ == '__main__':
    main()