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
    macierz=macierz_Hilberta(3)
    macierz_B=[[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]
    #print(f"macierz Hilberta to: {macierz}")
    #print(f"slad macierzy: {macierz_B} to: {znajdz_slad(macierz_B)}")
    #print(f"macierz: {macierz} jest: {czy_symetryczna(macierz)}")
    #print(f"macierz: {macierz} jest: {znajdz_diagonale(macierz_B)}")
    k=3
    macierz_c=[[1,0,0],[0,1,0],[0,0,1]]
    x=[1,3,5,7,78,4,2,4,7]
    y=[2,5,8]
    #print(f"macierz: {macierz_B} pomnozona przez {k} jest rowna: {mnozenie_przez_skalar(macierz,k)}")
    #print(f"macierzA pomnozona przez macierzB jest rowna: {mnozenie_macierzy(macierz_c,macierz)}")
    #print(f"wektor X pomnozony przez wektor Y jest rowny: {outer_product(x,y)}")
    #print(f"macierz transponowana to: {tworzenie_transpozycji(macierz)}")
    #print(f"macierzA poszerzona o wiersz b jest rowna: {dodanie_wiersza_do_macierzy(macierz_c, y, k)}")
    #print(f"macierzA poszerzona o kolumne b jest rowna: {dodanie_kolumny_do_macierzy(macierz_c, y, k)}")
    #print(f"macierzA usunietao kolumne b jest rowna: {usunięcie_wiersza_i_kolumny(macierz_c, 0, 0)}")
    print(f"macierzA usunietao kolumne b jest rowna: {czy_kwadrat_magiczny(macierz_c)}")


def macierz_Hilberta(n):
    lista=[None for i in range(n)]
    macierz=[None for i in range(n)]
    for i in range(n):
        wiersz = lista.copy()
        for j in range(n):
            element=1/(i+j+1)
            wiersz[j]=element
        macierz[i]=wiersz
    return macierz

def znajdz_slad(macierz_A):
    slad=0
    for i in range(len(macierz_A)):
        wiersz=macierz_A[i]
        slad+=wiersz[i]
    return slad

def czy_symetryczna(macierz_A):
    wynik="symetryczna"
    for i in range(len(macierz_A)):
        wiersz=macierz_A[i]
        for j in range(len(wiersz)):
            if i==j:
                break
            elem1=wiersz[j]
            wiersz2=macierz_A[j]
            elem2=wiersz2[i]
            if elem2!=elem1:
                wynik="niesymetryczna"
                return wynik
    return wynik

def znajdz_diagonale(macierz_A):
    diagonala=[None for i in range(len(macierz_A))]
    for i in range(len(macierz_A)):
        wiersz=macierz_A[i]
        diagonala[i]=wiersz[i]
    return diagonala

def mnozenie_przez_skalar(macierz, k):
    for i in range(len(macierz)):
        wiersz=macierz[i]
        for j in range(len(wiersz)):
            wiersz[j]*=k
    return macierz

def mnozenie_macierzy(macierz_A, macierz_B):
    n=len(macierz_A)
    m=len(macierz_B[0])
    x=len(macierz_B)
    lista = [None for i in range(m)]
    macierzW = [None for i in range(n)]
    for i in range(n):
        wierszA = lista.copy()
        wierszA=macierz_A[i]
        wierszW = lista.copy()
        for j in range(m):
            elemW=0
            for k in range(x):
                elemA=wierszA[k]
                wierszB = lista.copy()
                wierszB=macierz_B[k]
                elemB=wierszB[j]
                elemW+=elemA*elemB
            wierszW[j]=elemW
        macierzW[i] = wierszW
    return macierzW

def outer_product(x,y):
    n=len(x)
    m=len(y)
    lista = [None for i in range(m)]
    macierzW = [None for i in range(n)]
    for i in range(n):
        elemx=x[i]
        wierszw=lista.copy()
        for j in range(m):
            elemy=y[j]
            elemw=elemx*elemy
            wierszw[j]=elemw
        macierzW[i]=wierszw
    return macierzW

def tworzenie_transpozycji(macierzA):
    n=len(macierzA)
    m=len(macierzA[0])
    lista = [None for i in range(n)]
    macierzW = [None for i in range(m)]
    for i in range(m):
        wierszw=lista.copy()
        for j in range(n):
            wierszw[j]=(macierzA[j])[i]
        macierzW[i]=wierszw
    return macierzW

def dodanie_wiersza_do_macierzy(macierzA, listab,indeks):
    n=len(macierzA)
    m=len(macierzA[0])
    lista = [None for i in range(m)]
    macierzW = [None for i in range(n+1)]
    licznik=0
    for i in range(n):
        if i==indeks:
            macierzW[i]=listab
            licznik=1
            continue
        wierszA=lista.copy()
        wierszA=macierzA[i-licznik]
        macierzW[i]=wierszA
    if licznik==0:
        macierzW[n]=listab
    else:
        macierzW[n]=macierzA[n-1]
    return macierzW

def dodanie_kolumny_do_macierzy(macierzA, listab, indeks):
    n = len(macierzA)
    m = len(macierzA[0])
    lista = [None for i in range(m+1)]
    macierzW = [None for i in range(n)]
    for i in range(n):
        wierszA=lista.copy()
        wierszA=macierzA[i]
        wierszW=lista.copy()
        licznik = 0
        for j in range(m+1):
            if j==indeks:
                elemw=listab[i]
                licznik=1
            else:
                elemw=wierszA[j-licznik]
            wierszW[j]=elemw
        macierzW[i]=wierszW
    return macierzW

def usunięcie_wiersza_i_kolumny(macierz_A, k, l):
    n= len (macierz_A)
    m= len (macierz_A[0])
    macierz_W= [None for i in range(n-1)]
    licznikw =0
    for i in range (n):
        if i==k:
            licznikw=1
            continue
        wierszw= [None for i in range (m-1)]
        licznikk=0
        for j in range (m):
            if j==l:
                licznikk= 1
                continue
            elemw= macierz_A[i][j]
            wierszw[j- licznikk]= elemw
        macierz_W[i- licznikw]= wierszw
    return macierz_W

def czy_kwadrat_magiczny(macierzA):
    wynik = "jest"
    n= len(macierzA)
    m=len(macierzA[0])
    if n!=m:
        return "nie jest"
    sumap=0
    for i in range (n):
        wiersz= macierzA[i]
        sumaw=0
        for j in range(m):
            sumaw+=wiersz[j]
        if i!=0:
            if sumap!= sumaw:
                wynik ="nie jest"
                return wynik
        sumap=sumaw
    suma1=0
    suma2=0
    for i in range(n):
        suma1+=macierzA[i][i]
        suma2+=macierzA[i][n-1-i]
    if suma1!=suma2:
        return "nie jest"
    if suma1!=sumap:
        return "nie jest"
    return wynik

if __name__ == '__main__':
    main()