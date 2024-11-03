import numpy
from PIL import Image
import math
import csv



def main():
    cechy = []
    f = open("train_wine.csv", "r")  # r=do odczytu
    for row in csv.reader(f):
        for i in range(len(row)):
            row[i] = float(row[i])  # konwersja z str na float
        list.append(cechy, row)  # == A.append(row)
    f.close()
    if len(cechy)==0:
        raise Exception
    for i in cechy:
        if type(i)!=list:
            raise Exception
        if len(i)!=2:
            raise Exception
    print(cechy)


    wektor_klas=[]
    with open ("train_class.txt", "r") as plik_z_klasa:
        for linia in plik_z_klasa:
            linia=int(linia)
            if linia != 1 and linia!=0:
                raise Exception
            wektor_klas.append(linia)
    if len(wektor_klas)!=len(cechy):
        raise Exception
    print(wektor_klas)
    nowy_wektor=[12.5, 2]
    macierz_wektorow=[[12,3],[13,3], [12.5, 2.5],[11, 1.5]]
    #print(distance(wektor_klas, wektor_klas))
    print(f"klasa z to: {nearest_neighbor_class(cechy,wektor_klas, nowy_wektor)}")
    print(f"klasy z to: {knn(cechy,wektor_klas, macierz_wektorow)}")

    return


def distance(u, v):
    m=len(u)
    wynik=0
    suma=0
    for i in range(m):
        suma+=(u[i]-v[i])**2
    wynik=math.sqrt(suma)
    return wynik

def nearest_neighbor_class(macierz_cech, wektor_klas, wektor_nowego_wina):
    minimalna_odleglosc=float("inf")
    klasa=0
    for i in range(len(macierz_cech)):
        odleglosc=distance(macierz_cech[i], wektor_nowego_wina)
        if odleglosc<minimalna_odleglosc:
            minimalna_odleglosc=odleglosc
            klasa=wektor_klas[i]
    return klasa

def knn(macierz_cech, wektor_klas, macierz_nowych_win):
    klasy_nowych_win=[None for i in range(len(macierz_nowych_win))]
    for i in range(len(macierz_nowych_win)):
        wektor_wina=macierz_nowych_win[i]
        klasy_nowych_win[i]=nearest_neighbor_class(macierz_cech, wektor_klas, wektor_wina)
    return klasy_nowych_win


if __name__ == '__main__':
    main()