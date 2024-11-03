'''
cwiczenia zestaw nr 3
'''
import csv

def main():
    alergeny = wczytaj_dane()
    print(alergeny)
    wypisz_dane(alergeny)
    lista1=[0,10,5]
    lista2=[1,2,3,8]
    k=5
    print("")
    print(szukaj_bezpiecznych_dan(alergeny, lista1))
    print("")
    #print(stworzenie_wektora_nowego_dania(alergeny, lista2))
    nowa_macierz=dodaj_nowe_danie(alergeny,lista2)
    wypisz_dane(nowa_macierz)
    print("")
    mniejsza_macierz=usun_najgorsz(nowa_macierz,k)
    wypisz_dane(mniejsza_macierz)
    zapisz_informacje(mniejsza_macierz, "zapis.txt")
    return

def wczytaj_dane():
    M = []
    f = open("alerg.csv")
    for row in csv.reader(f):
        for i in range(len(row)):
            row[i] = int(row[i])  # konwersja z str na int
        list.append(M, row)  # == A.append(row)
    f.close()
    return M

def wypisz_dane(dane):
    for i in range(-1,len(dane)):
        for j in range(-1, len(dane[0])):
            if i==-1 and j==-1:
                print(f"{'':<4s}",end="")
                continue
            elif i==-1:
                print(f"{j:^3d}", end="")
                continue
            if j==-1:
                print(f"{f'{i}:':^4s}",end="")
                continue
            elem=dane[i][j]
            print(f"{elem:^3d}",end="")
        print("")

def szukaj_bezpiecznych_dan(dane, lista):
    czy_brak_alergenow=[0 for i in range(len(dane))]
    ile_pasujacych=0
    for i in range(len(dane)):
        czy_zawiera=0
        for j in lista:
            if dane[i][j]==1:
                czy_zawiera=1
                break
        if czy_zawiera==0:
            czy_brak_alergenow[i]=1
            ile_pasujacych+=1
    bezpieczne_dania=[None for i in range(ile_pasujacych)]
    licznik=0
    for i in range(len(czy_brak_alergenow)):
        if czy_brak_alergenow[i]==1:
            bezpieczne_dania[licznik]=i
            licznik+=1
    return bezpieczne_dania

def stworzenie_wektora_nowego_dania(dane,lista):
    n=len(dane[0])
    wektor=[0 for i in range(n)]
    for i in lista:
        wektor[i]=1
    return wektor

def dodaj_nowe_danie(dane, lista):
    wektor=stworzenie_wektora_nowego_dania(dane, lista)
    macierz_z_nowym_daniem=[None for i in range(len(dane)+1)]
    for i in range(len(macierz_z_nowym_daniem)):
        if i<len(dane):
            macierz_z_nowym_daniem[i]=dane[i]
        else:
            macierz_z_nowym_daniem[i]=wektor
    return macierz_z_nowym_daniem

def ilosc_alergenow(dane,k=5):
    ile_alergenow = [None for i in range(len(dane))]
    licznik = 0
    for i in range(len(dane)):
        suma = 0
        for j in range(len(dane[0])):
            if dane[i][j] == 1:
                suma += 1
        if suma >= k:
            licznik += 1
        ile_alergenow[i] = suma
    return ile_alergenow, licznik

def usun_najgorsz(dane,k):
    ile_alergenow, licznik=ilosc_alergenow(dane,k)
    nowa_macierz=[None for i in range(len(dane)-licznik)]
    licznik=0
    for i in range(len(dane)):
        if ile_alergenow[i]>=k:
            continue
        else:
            nowa_macierz[licznik]=dane[i]
            licznik+=1
    return nowa_macierz

def ile_dan_z_iloma_alergenami(ile_alergenow, liczba_uwzglednionych_alergenow):
    ilosci_takich_dan=[0 for i in range(liczba_uwzglednionych_alergenow)]
    for i in ile_alergenow:
        ilosci_takich_dan[i]+=1
    for i in range(len(ilosci_takich_dan)-1,-1,-1):
        if ilosci_takich_dan[i]>0:
            maksymalna=i
            break
    return ilosci_takich_dan, maksymalna

def zapisz_informacje(dane, sciezka):
    liczba_dan=len(dane)
    liczba_uwzgednionych_alergenow=len(dane[0])
    ile_alergenow, k =ilosc_alergenow(dane)
    ilosci_takich_dan, maksymalna=ile_dan_z_iloma_alergenami(ile_alergenow, liczba_uwzgednionych_alergenow)
    with open (sciezka,"w") as podsumowanie:
        podsumowanie.write(f"liczba dan: {liczba_dan}\n")
        podsumowanie.write(f"liczba uwzglednionych alergenow: {liczba_uwzgednionych_alergenow}\n")
        podsumowanie.write(f"maksymalna liczba alergenow w jednym daniu: {maksymalna}\n")
        for i in range(maksymalna+1):
            podsumowanie.write(f"liczba dan z {i} alergenami: {ilosci_takich_dan[i]}\n")



if __name__ == '__main__':
    main()