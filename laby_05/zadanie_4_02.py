'''
laby nr 4
zadanie 1
'''
import random
import math
def main():
    n=int(input("podaj n: "))
    print(f"pi to : {przyblizPi(n)}")
    print(f"roznica z obliczona waroscia pi wynosi: {math.pi - przyblizPi(n)}")
    return



def przyblizPi(n):
    w_kolku = 0
    for i in range(n):
        x=random.uniform(-1,1)
        y=random.uniform(-1,1)
        odleglosc = math.sqrt((x**2) + (y**2))

        if odleglosc<=1:
            w_kolku+=1
    frakcja=(w_kolku/n)


    return (frakcja*4)

if __name__ == '__main__':
    main()