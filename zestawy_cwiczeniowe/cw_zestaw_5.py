'''
cwiczenia zestaw nr 3
'''

import math
import random

def main():
    lista1=[1,2,3,4,5]
    lista2=[5,4,3,2,1]
    k=2
    lista3=[1,2,3]
    lista4=[float("nan"), float("nan"),float("nan"),1,2,3,float("nan"),1,2,float("nan"),4]
    lista5=[0,0,1,2,0,3,4,0,0,0,5,0,0,3]
    lista6=[1,2,3,4,5,6,7,4,4,4,4,3,3,3,2,3,5]
    lista7=[1,1,1,2.2,2.2,2.2,3,3,3,4.5,5,5.6,77]
    macierz_c = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    macierz_B=[[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]
    macierzA=[[1,2,3,4,5],[2,3,4,5,1],[3,4,5,1,2],[4,5,1,2,3],[5,1,2,3,4]]
    #print(konkatenacja(lista1,lista2))
    #print(powielenie_elementu_k_razy(lista3,k))
    #print(trim_nan(lista4))
    #print(rm_dup(lista5))
    #print(wyznacz_dominante(lista6))
    #print(unique(lista7))
    x=[3,5,8,10,1,2,8,13]
    n=["a","a","b","c","a","b","d","c"]
    #print(czy_to_kwadrat_lacinski(macierzA))
    print(split_labels(x,n))


def konkatenacja(lista1, lista2):
    n=len(lista1)
    m=len(lista2)
    wynik=[None for i in range(n+m)]
    for i in range(n):
        wynik[i]=lista1[i]
    for i in range(n,n+m):
        wynik[i]=lista2[i-n]
    return wynik

def powielenie_k_razy(lista, k):
    n=len(lista)
    wynik=[None for i in range(int(n*k))]
    for i in range(len(wynik)):
        wynik[i]=lista[i%n]
    return wynik

def powielenie_elementu_k_razy(lista, k):
    n=len(lista)
    wynik = [None for i in range(int(n * k))]
    for i in range(len(wynik)):
        wynik[i]=lista[i//2]
    return wynik

def trim_nan(lista):
    ilosc_nan_z_przodu=0
    ilosc_nan_z_tylu=0
    for i in range(len(lista)//2):
        if math.isnan(lista[i]):
            ilosc_nan_z_przodu+=1
        else:
            break
    for i in range(len(lista) // 2):
        elem=lista[len(lista)-1-i]
        if math.isnan(elem):
            ilosc_nan_z_tylu+=1
        else:
            break
    wynik=[None for i in range(len(lista)-ilosc_nan_z_tylu-ilosc_nan_z_przodu)]
    indeks=0
    for i in range(ilosc_nan_z_przodu, len(lista)-ilosc_nan_z_tylu):
        wynik[indeks]=lista[i]
        indeks+=1
    return wynik

def rm_nan(lista):
    czy_nan= [0 for i in range(len(lista))]
    ilosc_nan=0
    for i in range(len(lista)):
        if math.isnan(lista[i]):
            czy_nan[i]=1
            ilosc_nan+=1
    wynik = [None for i in range(len(lista) - ilosc_nan)]
    indeks = 0
    for i in range(len(lista)):
        if czy_nan[i]==0:
            wynik[indeks] = lista[i]
            indeks += 1
    return wynik

def rm_dup(lista):
    ilosc_powtarzajacych_sie_elementow=0
    lista_czy_sie_powtarza=[0 for i in range(len(lista))]
    for i in range(len(lista)-1):
        if lista[i]==lista[i+1]:
            lista_czy_sie_powtarza[i]=1
            ilosc_powtarzajacych_sie_elementow+=1
    wynik=[None for i in range(len(lista)-ilosc_powtarzajacych_sie_elementow)]
    indeks=0
    for i in range(len(lista)):
        if lista_czy_sie_powtarza[i]==0:
            wynik[indeks]=lista[i]
            indeks+=1
    return wynik

def wyznacz_dominante(lista):
    a=float("inf")
    b=float("-inf")
    for i in lista:
        if i>b:
            b=i
        if i<a:
            a=i
    ilosc_wystapien=[0 for i in range(b-a+1)]
    for i in range(len(lista)):
        ilosc_wystapien[lista[i]-a]+=1
    ilosc_najwiekszych=0
    indeksy_najwiekszych=[None for i in range(len(ilosc_wystapien))]
    najwiecej_powtorzen=0
    for i in range(len(ilosc_wystapien)):
        if ilosc_wystapien[i]>najwiecej_powtorzen:
            najwiecej_powtorzen=ilosc_wystapien[i]
    indeks=0
    for i in range(len(ilosc_wystapien)):
        if ilosc_wystapien[i]==najwiecej_powtorzen:
            ilosc_najwiekszych+=1
            indeksy_najwiekszych[indeks]=i
            indeks+=1
    if ilosc_najwiekszych==1:
        return lista[indeksy_najwiekszych[0]]
    indeks_indeksu_dominanty=random.randint(0,ilosc_najwiekszych-1)
    return lista[indeksy_najwiekszych[indeks_indeksu_dominanty]]

def unique(lista):
    wynik=rm_dup(lista)
    return wynik

def wyznaczanie_rang(lista):
    pass

def czy_to_kwadrat_lacinski(macierz):
    if len(macierz)!=len(macierz[0]):
        return "nie jest"
    n=len(macierz)
    for i in range(n):
        for j in range(n):
            if macierz[i][j]<1 or macierz[i][j]>n:
                return "nie jest"
            for k in range(j+1,n):
                if macierz[i][j]==macierz[i][k]:
                    return "nie jest"
    for i in range(n):
        for j in range(n):
            for k in range(i+1,n):
                if macierz[i][j]==macierz[k][j]:
                    return "nie jest"
    return "jest"


def split_labels(x, n):
    l=[]
    y=[]
    for i in range(len(n)):
        elem=n[i]
        czy_bylo=0
        for j in range(len(l)):
            if elem==l[j]:
                czy_bylo=1
                break
        if czy_bylo==1:
            continue
        podlista=[x[i]]
        for j in range(i+1,len(n)):
            if elem==n[j]:
                podlista.append(x[j])
        l.append(elem)
        y.append(podlista)
    return [l,y]



if __name__ == '__main__':
    main()