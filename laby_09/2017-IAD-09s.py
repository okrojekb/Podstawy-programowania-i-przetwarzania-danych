
import csv
import math
import matplotlib.pyplot as plt


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
    #print(f"klasa z to: {nearest_neighbor_class(cechy,wektor_klas, nowy_wektor)}")
    #print(f"klasy z to: {knn(cechy,wektor_klas, macierz_wektorow)}")
    x, y =generuj_listy_x_y(cechy)
    print(x,y)
    xy=zamiana_x_y_na_macierz(x,y)
    print(xy)
    klasa_macierzyxy=klasa_macierzy_xy(cechy, wektor_klas, xy)
    print(klasa_macierzyxy)
    #rysunek(x,y,klasa_macierzyxy, cechy, wektor_klas)

    cechy_testowe = []
    f = open("test_wine.csv", "r")  # r=do odczytu
    for row in csv.reader(f):
        for i in range(len(row)):
            row[i] = float(row[i])  # konwersja z str na float
        list.append(cechy_testowe, row)  # == A.append(row)
    f.close()
    print(cechy_testowe)
    klasy_testowe=knn(cechy, wektor_klas, cechy_testowe)
    print(klasy_testowe)

    wektor_klas_testowych = []
    with open("test_class.txt", "r") as plik_z_klasa:
        for linia in plik_z_klasa:
            linia = int(linia)
            if linia != 1 and linia != 0:
                raise Exception
            wektor_klas_testowych.append(linia)

    tworzenie_pliku_output(klasy_testowe, wektor_klas_testowych)

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

def generuj_ciag(minimalna, maksymalna, n=10):
    r=(maksymalna - minimalna)/(n-1)
    wynik=[None for i in range(n)]
    for i in range(n):
        wynik[i]=minimalna+(r*i)
    return wynik

def szukaj_minimalna_i_maksymalna(macierz):
    minimalna_1 = float("inf")
    minimalna_2 =float("inf")
    maksymalna_1= float("-inf")
    maksymalna_2= float("-inf")
    for i in macierz:
        if i[0]>maksymalna_1:
            maksymalna_1=i[0]
        if i[0]<minimalna_1:
            minimalna_1=i[0]
        if i[1]>maksymalna_2:
            maksymalna_2=i[1]
        if i[1]<minimalna_2:
            minimalna_2=i[1]
    return minimalna_1, maksymalna_1, minimalna_2, maksymalna_2

def generuj_listy_x_y(macierz):
    min1, maks1, min2, maks2 = szukaj_minimalna_i_maksymalna(macierz)
    x=generuj_ciag(min1, maks1)
    y=generuj_ciag(min2, maks2)
    return x, y

def zamiana_x_y_na_macierz(x,y):
    macierz=[None for i in range(len(x))]
    for i in range(len(x)):
        macierz_xi=[None for k in range(len(y))]
        for j in range(len(y)):
            macierz_xi[j]=[x[i],y[j]]
        macierz[i]=macierz_xi
    return macierz

def klasa_macierzy_xy(macierz_cech, wektor_klas,macierzxy):
    macierz_nowych_klas=[None for i in range(len(macierzxy))]
    for i in range(len(macierzxy)):
        macierz_nowych_klas[i]=knn(macierz_cech, wektor_klas, macierzxy[i])
    return macierz_nowych_klas

def zamiana_klas_na_kolory(klasy_macierzyxy):
    kolory=[None for i in range(len(klasy_macierzyxy))]
    for i in range(len(kolory)):
        if klasy_macierzyxy[i]==0:
            kolory[i]="r"
        else:
            kolory[i]="b"
    return kolory

def macierzxy_do_rysunku(x,y):
    wynik=[None for i in range(len(x)*len(y))]
    for i in range(len(x)):
        elemx=x[i]
        for j in range(len(y)):
            elemy=y[j]
            wynik[i*len(x)+j]=[elemx, elemy]
    return wynik

def zamiana_macierzy_klas_na_liste(klasa_macierzy_xy):
    n=len(klasa_macierzy_xy)
    m=len(klasa_macierzy_xy[0])
    lista=[None for i in range(n*m)]
    for i in range(n):
        for j in range(m):
            lista[m*i+j]=klasa_macierzy_xy[i][j]
    return lista

def rysunek(x, y, klasa_macierzy_xy, macierz_cech, wektor_klas):
    macierz_do_rysunku=macierzxy_do_rysunku(x,y)
    lista_klas=zamiana_macierzy_klas_na_liste(klasa_macierzy_xy)
    kolory=zamiana_klas_na_kolory(lista_klas)
    fig = plt.figure()
    for i in range(len(macierz_do_rysunku)):
        elemx=macierz_do_rysunku[i][0]
        elemy=macierz_do_rysunku[i][1]
        kolor=kolory[i]
        plt.scatter(elemx, elemy, color=kolor, alpha=0.5, marker=".")  # dla list u i v (o takim samym rozmiarze)
    kolory = zamiana_klas_na_kolory(wektor_klas)
    for i in range(len(macierz_cech)):
        elemx = macierz_cech[i][0]
        elemy = macierz_cech[i][1]
        kolor = kolory[i]
        plt.scatter(elemx, elemy, color=kolor)  # dla list u i v (o takim samym rozmiarze)
    fig.savefig("output.png", dpi=90)

def porownywanie_wynikow(klasy_testowe, wektor_klas_testowych):
    TN=0
    FP=0
    FN=0
    TP=0
    for i in range(len(klasy_testowe)):
        if klasy_testowe[i]==0:
            if wektor_klas_testowych[i]==0:
                TN+=1
            else:
                FN+=1
        else:
            if wektor_klas_testowych[i]==0:
                FP+=1
            else:
                TP+=1
    return TN, FP, FN, TP

def dokladnosc(TN, FP, FN, TP):
    licznik=TP + TN
    mianownik = TN + FP + FN + TP
    wynik=licznik/mianownik
    return wynik

def precyzja(TP, FP):
    wynik=TP/(TP + FP)
    return wynik

def czulosc(TP, FN):
    wynik=TP/(TP+FN)
    return wynik

def miaraF1(TP,FP,FN):
    wynik=(2*TP)/(2*TP + FP + FN)
    return wynik

def tworzenie_pliku_output(klasy_testowe, wektor_klas_testowych):
    TN, FP, FN, TP = porownywanie_wynikow(klasy_testowe, wektor_klas_testowych)
    with open ("output.txt", "w") as plik_oceny_klasyfikatora:
        for i in range(4):
            if i==1:
                for j in range(17):
                    plik_oceny_klasyfikatora.write("-")
                plik_oceny_klasyfikatora.write("\n")
                continue

            for j in range(5):
                if j==1 or j==3:
                    plik_oceny_klasyfikatora.write(f"|")
                elif i==0:
                    if j==2:
                        plik_oceny_klasyfikatora.write(f"{0:^7d}")
                    if j==4:
                        plik_oceny_klasyfikatora.write(f"{1:^7d}\n")
                    if j==0:
                        plik_oceny_klasyfikatora.write("  ")
                elif i==2 and j==0:
                    plik_oceny_klasyfikatora.write(f"{0:<2d}")
                elif i==3 and j==0:
                    plik_oceny_klasyfikatora.write(f"{1:<2d}")
                elif i==2:
                    if j==2:
                        plik_oceny_klasyfikatora.write(f"{TN:^7d}")
                    if j == 4:
                        plik_oceny_klasyfikatora.write(f"{FP:^7d}\n")
                elif i==3:
                    if j==2:
                        plik_oceny_klasyfikatora.write(f"{FN:^7d}")
                    if j == 4:
                        plik_oceny_klasyfikatora.write(f"{TP:^7d}\n")
        plik_oceny_klasyfikatora.write("\n")
        dokladn = dokladnosc(TN, FP, FN, TP)
        plik_oceny_klasyfikatora.write(f"{'Dokladnosc':<10s} = {dokladn:^5.2f}\n")
        prec= precyzja(TP, FP)
        plik_oceny_klasyfikatora.write(f"{'Precyzja':<10s} = {prec:^5.2f}\n")
        czul = czulosc(TP, FN)
        plik_oceny_klasyfikatora.write(f"{'Czulosc':<10s} = {czul:^5.2f}\n")
        miara=miaraF1(TP, FP, FN)
        plik_oceny_klasyfikatora.write(f"{'Miara F1':<10s} = {miara:^5.2f}\n")
    return

if __name__ == '__main__':
    main()