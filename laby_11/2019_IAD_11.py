def main():
    dane=wczytaj()
    print(dane)
    y=[1,2,1,3,4,2,4,6,8,1,0]
    a=[1,4,5,8,9]
    b=[1,1,1,3,6,7,8,99]


    podzielone_dane=(podziel(dane))
    #print(podzielone_dane)
    wypisz(podzielone_dane)
    print(zlacz_posortowane(podzielone_dane))

def wczytaj():
    with open ("dane.txt", "r") as plik_z_danymi:
        dane=[]
        for linia in plik_z_danymi:
            linia=int(linia)
            if linia>=0:
                dane.append(int(linia))
    return dane

def sprawdz_poprawnosc(y):
    if len(y)==0:
        return False
    for i in range(len(y)):
        if type(y[i])!=int:
            return False
        elem=int(y[i])
        if elem<0:
            return False
    return True

def podziel(y):
    if not sprawdz_poprawnosc(y):
        raise Exception
    wynik=[]
    podzbior=[]
    poprz=float("-inf")
    for i in range(len(y)):
        if y[i]>poprz:
            podzbior.append(y[i])
            poprz=y[i]
        else:
            poprz = y[i]
            wynik.append(podzbior)
            podzbior=[y[i]]
    wynik.append(podzbior)
    return wynik

def wypisz(x):
    podzielone_na_podciagi=x
    for i in range(len(podzielone_na_podciagi)):
        print(f"x[{i:^5d}]",end="")
        for j in podzielone_na_podciagi[i]:
            print(f"{j:^7d}",end="")
        print("")

def polacz(x,y):
    wynik=[]
    ind_x=0
    ind_y=0
    while ind_x<len(x) or ind_y<len(y):
        if ind_x>=len(x):
            wynik.append(y[ind_y])
            ind_y+=1
            continue
        if ind_y>=len(y):
            wynik.append(x[ind_x])
            ind_x+=1
            continue
        if x[ind_x]==y[ind_y]:
            wynik.append(x[ind_x])
            wynik.append(y[ind_y])
            ind_x+=1
            ind_y+=1
            continue
        if x[ind_x]>y[ind_y]:
            wynik.append(y[ind_y])
            ind_y+=1
            continue
        if x[ind_x]<y[ind_y]:
            wynik.append(x[ind_x])
            ind_x+=1
            continue
    return wynik


def zlacz_posortowane(x):
    poprzednia=x[0]
    for i in range(1,len(x)):
        poprzednia=polacz(poprzednia,x[i])
    return poprzednia




if __name__ == '__main__':
        main()