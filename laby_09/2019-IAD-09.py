
import csv
import math
import matplotlib.pyplot as plt
import csv

def main():
    studenci=wczytaj_csv()
    print(studenci)
    popraw(studenci)
    print(studenci)
    wypisz(studenci)
    tabela_ocen=oceny(studenci)
    wypisz_tabele_ocen(tabela_ocen)
    statystyki(studenci)

def wczytaj_csv():
    studenci = []
    with open("studenci.csv") as f:
        for row in csv.reader(f):
            studenci.append(row)
    return studenci

def popraw(studenci):
    for i in range(len(studenci)):
        wiersz=studenci[i]
        suma=0
        ilosc_pustych=0
        indeks_bez_oceny=-1
        for j in range(2,8):
            if j==2:
                wiersz[j]=int(wiersz[j])
                continue
            if wiersz[j]=='':
                if indeks_bez_oceny==-1:
                    indeks_bez_oceny=j
                    ilosc_pustych+=1
                else:
                    wiersz[j]=float("0")
                    ilosc_pustych+=1
            else:
                wiersz[j]=float(wiersz[j])
                suma+=wiersz[j]
        if ilosc_pustych==1:
            wiersz[indeks_bez_oceny]=suma/4
        if ilosc_pustych>1:
            wiersz[indeks_bez_oceny]=float("0")
        studenci[i]=wiersz

def wypisz(studenci):
    for i in studenci:
        print("| ",end="")
        for j in range(len(i)):
            if j>=0 and j<2:
                print(f"{i[j]:^12s}", end="")
            if j==2:
                print(f"{i[j]:^12d}", end="")
            if j>2:
                print(f"{i[j]:^8.1f}", end="")
        print("|")

def ktore_ocena(suma):
    if suma<=50:
        a=2
    elif suma<=60:
        a=3
    elif suma<=70:
        a=3.5
    elif suma<=80:
        a=4
    elif suma<=90:
        a=4.5
    elif suma<=1000:
        a=5
    return float(f"{a}")

def oceny(studenci):
    tabela_ocen=[None for i in range(len(studenci))]
    for i in range(len(studenci)):
        wiersz=[None, None]
        suma=0
        for j in range(2,len(studenci[0])):
            if j==2:
                wiersz[0]=studenci[i][j]
                continue
            suma+=studenci[i][j]
        wiersz[1]=ktore_ocena(suma)
        tabela_ocen[i]=wiersz
    return tabela_ocen

def wypisz_tabele_ocen(tabela_ocen):
    for i in tabela_ocen:
        print("|", end="")
        for j in range(2):
            if j==0:
                print(f"{i[j]:^14d}", end="")
            else:
                print(f"{i[j]:^8.1f}", end="")
        print("|")

def min_maks_sred(studenci, numer_zadania):
    minimalna=float("inf")
    maksymalna=float("-inf")
    suma=0
    for i in range(len(studenci)):
        elem=studenci[i][numer_zadania+2]
        if elem<minimalna:
            minimalna=elem
        if elem>maksymalna:
            maksymalna=elem
        suma+=elem
    srednia=suma/len(studenci)
    return minimalna,maksymalna, srednia



def statystyki(studenci):
    for i in range(1,6):
        print("|", end="")
        for j in range(4):
            if j==0:
                print(f"{i:^11d}", end="")
                continue
            minimalna, maksymalna, srednia = min_maks_sred(studenci, i)
            if j==1:
                print(f"{maksymalna: ^7.1f}", end="")
            elif j==2:
                print(f"{minimalna: ^7.1f}",end="")
            elif j==3:
                print(f"{srednia: ^7.1f}",end="")
        print("|")


if __name__ == '__main__':
    main()