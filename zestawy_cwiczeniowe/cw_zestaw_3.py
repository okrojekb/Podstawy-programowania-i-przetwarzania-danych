'''
cwiczenia zestaw nr 3
'''

def main():
    lista=[3,4,7,3,7,4,8,4,3,1,6,9,4,8,0,65,3,2,65,75,78,526,874,7875,541,51,46,47586,32,0]
    #print(f"minmax to: {min_i_max(lista)}")
    x=[2,2,2,4,5,7,8,11,11,11,12,14,14]
    y=[1,2,3,4,3,2,1]
    z=[1, float("NaN"), 3, float("NaN"), float("NaN"), 5]
    #print(f"czy lista jest posortowana {is_sorted(x)}")
    #print(f"K ty element to: {ktynajwiekszy(lista, 5)}")
    #print(f"Czy jest palindromem: {czy_palindrom(y)}")
    #print(f"Zamiana to: {zam_nan(z)}")
    print(f"n-ty element ciagu Golomba to: {n_ciag_golomba(12)}")


def n_ciag_golomba(n):
    if n<3:
        return n
    licznik=2
    cyfra=2
    indeks=3
    ciag=[0]*(n+1)
    ciag[1]=1
    ciag[2]=2
    while indeks<=n:
        ilosc_powt=ciag[cyfra]
        while licznik<ilosc_powt and indeks<n:
            ciag[indeks]=cyfra
            licznik+=1
            indeks+=1
        if licznik==ilosc_powt or indeks==n:
            ciag[indeks] = cyfra
            licznik = 1
            cyfra+=1
            indeks += 1
    return ciag[n]

def zam_nan(lista):
    liczba_l=0
    liczba_p=0
    wynik=[0]*len(lista)
    poprz=0
    for i in range(len(lista)):
        if lista[i]!=lista[i]:
            for j in range(i+1, len(lista)):
                if lista[j]==lista[j]:
                    liczba_p=lista[j]
                    break
            wynik[i]=(liczba_l+liczba_p)//2

        else:
            liczba_l=lista[i]
            wynik[i]=lista[i]
    return wynik

def czy_palindrom(lista):
    pol_dlugosci=len(lista)//2
    numer_od_tylu=len(lista)-1
    for i in range(pol_dlugosci):
        if lista[i]!=lista[numer_od_tylu-i]:
            return False
    return True



def min_i_max(lista):
    maximin=[lista[0],lista[0]]
    for i in lista:
        if i>=maximin[1]:
            maximin[1]=i
        if i<=maximin[0]:
            maximin[0]=i
    return maximin

def is_sorted(x):
    min=x[0]
    for i in x:
        if min<=i:
            min=i
        else:
            return False
    return True

def ktynajwiekszy(t, k):
    lista=[float("-inf")]*k
    for i in range (len(t)):
        elem=t[i]
        for j in range (k):
            if elem>=lista[j]:
                poprz_elem=lista[j]
                lista[j]=elem
                elem=poprz_elem
    return lista[k-1]

if __name__ == '__main__':
    main()