'''
laby nr 4
zadanie 1
'''


def main():
    print("Podaj dane zbioru B")
    listaB = podaj()
    print("Zbior B to:")
    wypisz(listaB)
    print("Podaj dane zbioru A")
    listaA = podaj()
    print("Zbior A to:")
    wypisz(listaA)
    elem=int(input("Podaj nowy element zbioru A: "))
    print(f"Zbior A po dodaniu elementu to:")
    listaA = dodaj(listaA, elem)
    wypisz(listaA)

    #listaA=[0,3,0,4]
    #listaB=[1,2,2,4]
    czesc_wspolna=przeciecie(listaA, listaB)
    roznic=roznica(listaA, listaB)
    print(f"Roznica to: ")
    wypisz(roznic)
    print(f"przeciecie: ")
    wypisz(czesc_wspolna)





    return

def podaj():
    maks_ele=int(input("Podaj maksymalny element przechowywany w multizbiorze: "))
    lista=[0]*(maks_ele+1)
    for i in range(maks_ele+1):
        lista[i]=int(input(f"Podaj {i}-ty element listy reprezentujacej multizbior: "))
    if lista[len(lista)-1]==0:
        raise ValueError("Bledne dane")
    return lista

def wypisz(lista):
    suma=0
    for elem in lista:
        suma+=elem
    multizbior=[0]*suma
    licznik=1
    cyfra=0
    for i in range(len(multizbior)):
        while True:
            if lista[cyfra]==0:
                cyfra+=1
            elif lista[cyfra]==licznik:
                multizbior[i]=cyfra
                licznik=1
                cyfra+=1
                break
            elif lista[cyfra]>licznik:
                multizbior[i]=cyfra
                licznik+=1
                break
    print(f"{multizbior}")

def dodaj(lista, element=10):
    if element<len(lista):
        lista[element]+=1
        return lista
    else:
        wieksza=[0]*(element+1)
        for i in range(len(lista)):
            wieksza[i]=lista[i]
        wieksza[element]=1
    return wieksza

def przeciecie(zbiorA, zbiorB):
    wsp_min=0
    for i in range(min(len(zbiorA), len(zbiorB))-1,-1, -1):
        if zbiorB[i]>0 and zbiorA[i]>0:
            wsp_min=i
            break
    wynik=[0]*(wsp_min+1)
    for i in range(wsp_min+1):
        a=min(zbiorA[i], zbiorB[i])
        wynik[i]=a

    return wynik

def roznica(zbiorA, zbiorB):
    roz_min=0
    czesc_wspolna=przeciecie(zbiorA,zbiorB)
    if len(zbiorA)>len(zbiorB):
        roz_min=len(zbiorA)-1
    else:
        roz_min=len(czesc_wspolna)-1
        while True:
            if zbiorA[roz_min]==zbiorB[roz_min]:
                roz_min-=1
            else:
                break
    wynik=[0]*(roz_min+1)
    for i in range(roz_min+1):
        if i<len(czesc_wspolna):
            b=zbiorA[i]-czesc_wspolna[i]
            wynik[i]=b
        else:
            break
    for i in range(len(czesc_wspolna), roz_min+1):
        b=zbiorA[i]
        wynik[i]=b
    return wynik




if __name__ == '__main__':
    main()
