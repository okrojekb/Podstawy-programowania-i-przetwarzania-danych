"""
PPiPD ćwiczenia zestaw nr 1
Zadanie nr 1.1 py
"""
def main():
    '''
    a = int(input("podaj a"))
    b = int(input("podaj b"))
    c = int(input("podaj c"))
    d = int(input("podaj d"))
    print(f"NWD to {NWD(a,b)}")
    print(f"zamiana to {zamiana_dla_dwoch(a, b)}")
    print(f"zamiana dla trzech to {zamiana_dla_trzech(a,b,c)}")
    print(f"zamiana dla czterach to {zamiana_dla_czterech(a, b, c, d)}")
    print(f"kolejnosc dla trzech to {kolejnosc_dla_trzech(a, b, c)}")
    print(f"przeliczenia a to {przeliczenia_a(a, b, c)}")
    print(f"przeliczenia b to {przeliczenia_b(a, b, c)}")
    print(f"przeliczenia c to {przeliczenia_c(a, b, c)}")
    mnozenie =int(input("podaj a, gdzie (a*n)+b to n-ty wyraz ciagu "))
    dodawanie = int(input("podaj b, gdzie (a*n)+b to n-ty wyraz ciagu "))
    print(f"srednia arytmetyczna ciagu to {srednia_art_ciagu(b, mnozenie, dodawanie)}")
    print(f"srednia harmoniczna ciagu to {srednia_harm_ciagu(b, mnozenie, dodawanie)}")
    print(f"taki trojkat prostokatny {czy_prostokatny(a,b,c)}")
    print(f"taki trojkat  {czy_trojkat(a, b, c)}")
    print(f"rozwiązania tego rownania: {rozwiazanie_rownania(a,b,c)}")
    '''
    podstawa_systemu=int(input("Podaj podstawe systemu: "))
    x=int(input("Podaj liczbę x: "))
    print(f"minimalna liczba cyfr potrzebna do zapisu {x} w systemie {podstawa_systemu} -arnym to {min_liczba_cyfr(podstawa_systemu, x)}")
    return
def NWD (a,b): #zadanie 1.1
    while a != 0:
        c = b % a
        b = a
        a = c
    #print (f"NWD to {b}")
    return b
def zamiana_dla_dwoch (a,b): #zadanie 1.2
    c=a
    a=b
    b=c
    return (a,b)

def zamiana_dla_trzech (a,b,c): #zadanie 1.3
    d=a
    a=c
    c=b
    b=d
    return (a,b,c)

def zamiana_dla_czterech (a,b,c,d): #zadanie 1.4
    e=a
    a=c
    c=b
    b=d
    d=e
    return (a,b,c,d)

def kolejnosc_dla_trzech (a,b,c): #zadanie 1.5 i uzyte w zadanie 1.9 i 1.10
    d=a
    if b>d:
        e=b
    else:
        e=d
        d=b
    if c>e:
        f=c
    elif c>d:
        f=e
        e=c
    else:
        f=e
        e=d
        d=c
    return (d,e,f)

def przeliczenia_a (a,b,c): #zadanie 1.6a
    d=c
    c=a/b
    a=b
    b=d + 10
    return (a,b,c,b)

def przeliczenia_b(a,b,c): #zadanie 1.6b
    d=c
    a=a+b
    c=a+c
    b=d*d
    return (a,b,c)

def przeliczenia_c(a,b,c): #zadanie 1.6c
    d=b
    b=-a
    a=-b-d
    c=c+b+d
    return (a,b,c)

def n_wyraz_ciagu (n, mnozenie,dodawanie ): #część zadania 1.7 i 1.8
    return (n*mnozenie)+dodawanie

def srednia_art_ciagu(n, mnozenie, dodawanie): #zadanie 1.7
    srednia=0.0
    licznik=0
    while licznik<n:
        x=n_wyraz_ciagu(licznik, mnozenie, dodawanie)
        srednia= srednia + x
        licznik= licznik +1
    return srednia/n

def srednia_harm_ciagu (n, mnozenie, dodawanie): #zadanie 1.8
    srednia=0.0
    licznik=0
    while licznik<n:
        x=1/n_wyraz_ciagu(licznik, mnozenie, dodawanie)
        srednia+=x
        licznik=licznik +1
    return n/srednia

def czy_prostokatny (a,b,c): #zadanie 1.9
    boki=kolejnosc_dla_trzech(a,b,c)
    a=boki[0]
    b=boki[1]
    c=boki[2]
    if a**2 +b**2 ==c**2:
        wynik="istnieje"
    else:
        wynik="nieistnieje"
    return wynik

def czy_trojkat (a,b,c): # zadanie 1.10
    boki = kolejnosc_dla_trzech(a,b,c)
    a = boki[0]
    b = boki[1]
    c = boki[2]
    if a+b>c:
        wynik = "istnieje"
    else:
        wynik = "nieistnieje"
    return wynik
import math
def liczenie_delty (a,b,c): #czesc zadania 1.11
    d=b**2 - 4*a*c
    if d<0:
        wynik=-5
    else:
        wynik=math.sqrt(d)
    return wynik

def rozwiazanie_rownania(a,b,c): #zadanie 1.11
    if a==0:
        x=(-c)/b
        return x
    else:
        wynik_delty=liczenie_delty(a,b,c)
        if wynik_delty==0:
            x=(-b)/(2*a)
            return x
        elif wynik_delty>0:
            x=(-b+wynik_delty)/(2*a)
            y=(-b-wynik_delty)/(2*a)
            return (x,y)
        else:
            x="nie istnieja"
            return x

def min_liczba_cyfr(podstawa_systemu, x): #zadanie 1.15
    liczba_cyfr=0
    while (podstawa_systemu**liczba_cyfr)<=x:
        liczba_cyfr+=1

    return liczba_cyfr

if __name__ =='__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
