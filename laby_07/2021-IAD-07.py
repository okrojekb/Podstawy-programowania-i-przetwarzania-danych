'''
laby nr 4
zadanie 1
'''

import random

def main_A():
    dlugosc=int(input("Podaj dlugosc bazowa: "))
    if dlugosc<5 or dlugosc>15:
        raise ValueError("Bledne dane")
    random.seed(2014)
    pierwsza=losuj_litery(dlugosc)
    dlugosc = int(input("Podaj dlugosc bazowa: "))
    if dlugosc < 5 or dlugosc > 15:
        raise ValueError("Bledne dane")
    druga=losuj_litery(dlugosc)
    print(f"lista 1: {pierwsza}")
    print(f"lista 2: {druga}")
    print("\n")
    zawinieta=polacz_z_zawijaniem(pierwsza,druga)
    print(f"zawinienta to: {zawinieta}")
    print("\n")
    print(f"            druga to: {druga}")
    odwroc(druga, 3, 7)
    print(f"odwrocona lista 2 to: {druga}")
    print("\n")
    print(f"            pierwsza to: {pierwsza}")
    przesun_w_lewo(pierwsza, 3)
    print(f"przesunieta pierwsza to: {pierwsza}")
    print("\n")
    trzecia=['a','b','c','d']
    print(f"         trzecia to: {trzecia}")
    mod_26(trzecia)
    print(f"po mod26 trzecia to: {trzecia}")
    return

def losuj_litery(dlugosc):
    lista=[None]*dlugosc
    for i in range(dlugosc):
        numer_litery=random.randint(97,122)
        litera = chr(numer_litery)
        lista[i] = litera
    return lista

def polacz_z_zawijaniem(pierwsza, druga):
    zawinieta=[None]*(max(len(pierwsza),len(druga))*2)
    pol_dlugosci=len(zawinieta)//2
    for i in range(pol_dlugosci):
        zawinieta[i]=(pierwsza[i%len(pierwsza)])
    for j in range(pol_dlugosci):
        zawinieta[j+pol_dlugosci]=druga[j%len(druga)]
    return zawinieta

def odwroc(lista, indeks_startu, indeks_konca):
    ilosc_zamian=(indeks_konca-indeks_startu)//2
    for i in range(ilosc_zamian):
        lista[indeks_startu+i], lista[indeks_konca-i] = lista[indeks_konca-i], lista[indeks_startu+i]

def przesun_w_lewo(lista, ilosc_rotacji):
    for j in range(ilosc_rotacji):
        pomocnicza=lista[0]
        for i in range(len(lista)-1):
            lista[i]=lista[i+1]
        lista[len(lista)-1]=pomocnicza

def mod_26(tab):
    element_wczesniejszy=tab[0]
    suma =ord(tab[0]) + ord(tab[1])
    litera = chr((suma % 26) + 97)
    tab[0]=litera
    for i in range(1,len(tab)-1):
        suma=ord(element_wczesniejszy)+ord(tab[i])+ord(tab[i+1])
        litera=chr((suma%26)+97)
        element_wczesniejszy=tab[i]
        tab[i]=litera
    suma =ord(tab[len(tab)-1]) + ord(element_wczesniejszy)
    litera=chr((suma % 26) + 97)
    tab[len(tab)-1]=litera



if __name__ == "__main__":
    main_A()