'''
laby nr 4
zadanie 1
'''


def main():
    print("Podaj wymiary sadu: ")
    x_min = int(input("Podaj xmin: "))
    x_max = int(input("Podaj xmax: "))
    y_min = int(input("Podaj ymin: "))
    y_max = int(input("Podaj ymax: "))
    print(f"Podany prostokąt to: {wypisz_prostokat(x_min, x_max, y_min, y_max)}")
    a=najmniejszy_plot(x_min, x_max, y_min, y_max)[0]
    b=najmniejszy_plot(x_min, x_max, y_min, y_max)[1]
    c=najmniejszy_plot(x_min, x_max, y_min, y_max)[2]
    d=najmniejszy_plot(x_min, x_max, y_min, y_max)[3]
    print(f"Najmniejszy plot zawierajacy eszystkie drzewka: {wypisz_prostokat(a,b,c,d)}")
    print(f"Obwod sadu: {obwod_prostokata(x_min, x_max, y_min, y_max)}")
    print(f"Obwod plotu: {obwod_prostokata(a,b,c,d)}")


    with open("rysunek.txt", "w") as rysunek_sadu:
        for y in range(y_max, y_min - 2, -1):
            for x in range (x_min-1, x_max+1):
                if x==x_min-1 and y==y_min-1:
                    rysunek_sadu.write(f"{'y/x':<4s}")
                elif x==x_min-1:
                    rysunek_sadu.write(f"{y:<4d}")
                elif y==y_min-1:
                    rysunek_sadu.write(f"{x:<1d}")
                else:
                    if drzewo(x,y):
                        rysunek_sadu.write("D")
                    else:
                        rysunek_sadu.write(".")

            print("",file=rysunek_sadu)

    return

def wypisz_prostokat(x_min, x_max, y_min, y_max):
    print(f"[{x_min}, {x_max}]x[{y_min}, {y_max}]")

def najmniejszy_plot(x_min, x_max, y_min, y_max):
    czy_drzewo = 0
    while czy_drzewo==0 and x_min<x_max:
        for y in range (y_min, y_max+1):
            czy_tutaj = drzewo(x_min, y)
            if czy_tutaj:
                czy_drzewo+=1
                break
        if czy_drzewo==1:
            break
        else:
            x_min+=1
    if x_min==x_max:
        return (0,0,0,0)
    czy_drzewo=0
    while czy_drzewo==0 and x_min!=x_max:
        for y in range (y_min, y_max+1):
            czy_tutaj = drzewo(x_max, y)
            if czy_tutaj:
                czy_drzewo+=1
                break
        if czy_drzewo==1:
            break
        else:
            x_max-=1
    czy_drzewo=0
    while czy_drzewo==0 and y_min<y_max:
        for x in range (x_min, x_max+1):
            czy_tutaj = drzewo(x, y_min)
            if czy_tutaj:
                czy_drzewo+=1
                break
        if czy_drzewo==1:
            break
        else:
            y_min+=1
    if y_min==y_max:
        return (0,0,0,0)
    czy_drzewo=0
    while czy_drzewo==0 and y_min!=y_max:
        for x in range (x_min, x_max+1):
            czy_tutaj = drzewo(x, y_max)
            if czy_tutaj:
                czy_drzewo+=1
                break
        if czy_drzewo==1:
            break
        else:
            y_max-=1
    return x_min, x_max, y_min, y_max

def zapisz_do_plik (x_min, x_max, y_min, y_max, sciezka="rysunek.txt"):
    with open("rysunek.txt", "w") as rysunek_sadu:
        for y in range(y_max, y_min - 2):
            for x in range (x_min-1, x_max+1):
                if x==x_min-1:
                    rysunek_sadu.write(f"{y:<4d}")
    return

def obwod_prostokata(x_min,x_max,y_min,y_max):
    bok_a = x_max-x_min
    bok_b = y_max-y_min
    wynik=2*(bok_b+bok_a)
    return wynik

def najlepszy_podzial()

def drzewo(x, y):
    if x >= 0 and x <= 10 and y >= 0 and y <= 10:
        return (x == y) and (x % 10 < 4 or x % 10 > 5)
    elif x >= -10 and x <= -1 and y >= 0 and y <= 10:
        return True
    else:
        return False


if __name__ == '__main__':
    main()