"""
PPiPD ćwiczenia zestaw nr 2
Zadanie nr 1.2 py
"""
import math
def main():
    a = int(input("podaj liczbe a "))
    b = float(input("podaj liczbe b "))
    c = int(input("podaj liczbe c "))
    d = int(input("podaj liczbe d "))
    print (f"Mediana to {med3(a,b,c)}")
    print (f"maksimum {a},{b},{c},{d} to {max4(a,b,c,d)}")
    print(f"Pierwiastek to: {pierwiastek(a,b)}")
    print(f"iledzielnikow to : {ile_dzielnikow(a)}")
    print(f"Zamienione {a} to {zamiana_cyfr(a)}.")
    return

def med3(a,b,c): #zadanie 2.2
    d = a
    if b > d:
        e = b
    else:
        e = d
        d = b
    if c > e:
        f = c
    elif c > d:
        f = e
        e = c
    else:
        f = e
        e = d
        d = c
    return e

def max_2(a,b):
    max=a
    if b>a:
        max=b
    return max

def max4(a,b,c,d): #zadanie2.3
    max=a
    max=max_2(max,b)
    max = max_2(max, c)
    max = max_2(max, d)
    return max

def pierwiastek(x,E=1):
    przyblizenie2 = x
    przyblizenie1 = ((1 + x ) / 2)
    while przyblizenie2 - przyblizenie1>E:
        przyblizenie2=przyblizenie1
        przyblizenie1=((przyblizenie1+(x/przyblizenie1))/2)
    return przyblizenie1

def ile_dzielnikow(x):
    licznik=0
    pierwiastek_x = int(math.sqrt(x))

    for i in range(1,pierwiastek_x+1):
        if i*i == x:
            licznik += 1
            break
        elif x%i==0:
            licznik+=2
    return licznik

def zamiana_cyfr(x):
    zamieniona=0
    dlugosc=0
    while 10**dlugosc<=x:
        dlugosc +=1
    for i in range(1,dlugosc+1):
        zamieniona+=(x%(10))*(10**(dlugosc-i))
        x=x//(10)
    return zamieniona



if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
