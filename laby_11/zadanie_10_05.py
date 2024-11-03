import csv


def main():
    tips = []
    f = open("tips.csv", "r")  # r=do odczytu
    for row in csv.reader(f):
        tips.append(row)
    f.close()
    #print(tips)
    total_bill, tip, sex, smoker, day, time, size = dekompozycja_tips(tips)
    print(total_bill)
    #print(tip)
    #print(sex)
    #print(smoker)
    print(day)
    #print(time)
    #print(size)
    dict_day=unique(day)
    print(dict_day)
    print(unique(day))
    liczbowe_day=encode(day, dict_day)
    print(liczbowe_day)
    a=[8,10,16,32,3,1]
    b=[0,1,1,0,0,1]
    x=[1,2,3,4,5,5,6,6,6,6,7,7,8]
    print(split(total_bill, liczbowe_day, 4))
    #print(fivenum(x))


def dekompozycja_tips(macierz):
    total_bill=[None for i in range(len(macierz))]
    tip=[None for i in range(len(macierz))]
    sex=[None for i in range(len(macierz))]
    smoker=[None for i in range(len(macierz))]
    day=[None for i in range(len(macierz))]
    time=[None for i in range(len(macierz))]
    size=[None for i in range(len(macierz))]
    for i in range(len(macierz)):
        total_bill[i] = float(macierz[i][0])
        tip[i] = float(macierz[i][1])
        sex[i] = macierz[i][2]
        smoker[i] = macierz[i][3]
        day[i] = macierz[i][4]
        time[i] = macierz[i][5]
        size[i] =macierz[i][6]
    return total_bill, tip, sex, smoker, day, time,size

def unique(lista):
    wektor=[]
    for i in lista:
        ile_sprawdzonych=0
        for j in wektor:
            if i==j:
                break
            ile_sprawdzonych += 1
        if ile_sprawdzonych==len(wektor):
            wektor.append(i)
    return wektor

def encode(lista, wektor):
    wynik=[None for i in range(len(lista))]
    for i in range(len(lista)):
        elem=lista[i]
        for j in range(len(wektor)):
            if elem==wektor[j]:
                wynik[i]=j
                break
    return wynik

def split(lista1, lista2, n):
    wynik=[[] for i in range(n)]
    for i in range(len(lista2)):
        wynik[lista2[i]].append(lista1[i])
    return wynik

def mediana(pos_lista):
    n=len(pos_lista)
    if n%2==0:
        mediana=(pos_lista[n//2]+pos_lista[n//2+1])/2
    else:
        mediana=pos_lista[n//2]
    return mediana

def fivenum(lista1):
    wynik=[None for i in range(5)]
    lista1.sort()
    wynik[0]=lista1[0]
    wynik[4]=lista1[len(lista1)-1]
    med=mediana(lista1)
    wynik[2]=med
    p_polowa=[]
    for i in lista1:
        if i<med:
            p_polowa.append(i)
        else:
            break
    wynik[1]=mediana(p_polowa)
    d_polowa=[]
    for i in range(len(lista1)-1,-1,-1):
        if lista1[i]>med:
            d_polowa.append(lista1[i])
        else:
            break
    wynik[3]=mediana(d_polowa)
    return wynik

def boxplot1(lista1,lista2,dict_lista2):
    pass



if __name__ == '__main__':
        main()