import random
import  math

def main():
    random.seed(2022)
    #szerokosc_planszy=int(input("Podaj szerokosc planszy: "))
    szerokosc_planszy=5
    #wysokosc_planszy=int(input("Podaj szerokosc planszy: "))
    wysokosc_planszy=4
    #wysokosc_klocka=int(input("Podaj wysokosc klocka: "))
    wysokosc_klocka=2
    plansza=tworzenie_planszy(wysokosc_planszy, szerokosc_planszy)
    print("plansza")
    wypisz_macierz(plansza)
    while True:
        klocek=wylosuj_klocek(wysokosc_klocka,szerokosc_planszy)
        #print(klocek)
        print("Klocek")
        wypisz_macierz(klocek)
        macierz, czy=spusc_klocek(plansza,klocek)
        #print(maksym)
        print("plansza po dodaniu klocka")
        wypisz_macierz(macierz)
        if not czy:
            break


    return

def wypisz_macierz(M):
    for j in range(len(M[0]) + 2):
        print("-", end="")

    print()

    for i in range(len(M) - 1, -1, -1):
        print("|", end="")
        for j in range(len(M[i])):
            if M[i][j]:
                print("#", end="")
            else:
                print(" ", end="")
        print("|")
    for j in range(len(M[0]) + 2):
        print("-", end="")
    print()


def tworzenie_planszy(wysokosc, szerokosc):
    macierz=[None for i in range(wysokosc)]
    for i in range(wysokosc):
        wiersz=[False for j in range(szerokosc)]
        macierz[i]=wiersz
    return macierz

def odleglosc(x1,x2,y1,y2):
    wynik=math.sqrt((x1-x2)**2 + (y1-y2)**2)
    return wynik


def wylosuj_klocek(wysokosc, szerokosc):
    macierz=[None for i in range(wysokosc)]
    for i in range(wysokosc):
        wiersz=[False for j in range(szerokosc)]
        macierz[i]=wiersz
    kx=random.randint(0,szerokosc-1)
    ky=random.randint(0,wysokosc-1)
    d=0
    for i in range(wysokosc):
        for j in range(szerokosc):
            d=odleglosc(j,kx,i,ky)
            if random.random()<1/(d+1):
                macierz[i][j]=True
    return macierz

def spusc_klocek(plansza, klocek):
    lista_najnizszych_punktow_klocka=[None for l in range(len(plansza[0]))]
    for i in range(len(klocek)):
        for j in range(len(klocek[0])):
            if klocek[i][j] and lista_najnizszych_punktow_klocka[j]==None:
                lista_najnizszych_punktow_klocka[j]=i
    lista_najwyzszych_punktow_planszy=[None for l in range(len(plansza[0]))]
    for i in range(len(plansza)-1,-1,-1):
        for j in range(len(plansza[0])):
            if plansza[i][j]:
                lista_najwyzszych_punktow_planszy[j]=i
    maksymalny_spadek=-1
    for i in range(len(plansza[0])):
        elem1=lista_najwyzszych_punktow_planszy[i]
        elem2=lista_najnizszych_punktow_klocka[i]
        if elem1==None or elem2==None:
            continue
        maksymalny_spadek=max((elem1-elem2), (elem2-elem1))
    if maksymalny_spadek==-1:
        elem=float("inf")
        for i in lista_najnizszych_punktow_klocka:
            if i==None:
                continue
            if i<elem:
                maksymalny_spadek=len(plansza)-i
    maksymalny_spadek+=1
    powiekszony_klocek=[None for i in range(len(plansza)+len(klocek))]
    for i in range(len(powiekszony_klocek)):
        if i>=len(plansza):
            powiekszony_klocek[i]=klocek[i-len(plansza)]
        else:
            powiekszony_klocek[i]=[False for k in range(len(klocek[0]))]
    for i in range(len(plansza)):
        for j in range(len(plansza[0])):
            if plansza[i][j]:
                continue
            if i+maksymalny_spadek>=len(powiekszony_klocek):
                break
            plansza[i][j]=powiekszony_klocek[i+maksymalny_spadek][j]
    if len(plansza)+maksymalny_spadek<len(powiekszony_klocek):
        czy=False
    else:
        czy=True


    return plansza, czy

if __name__ == '__main__':
    main()