"""
PPiPD zajęcia drugie
zadanie 2.06 py
"""

def main():
    a=int(input("Podaj a: "))
    b = int(input("Podaj b: "))
    if a>=b:
        raise ValueError("a musi być mniejsze od b")
    if a<0 and b<2:
        print("w tym zakresie nie ma liczb pierwszych")
        return
    print(f"w zakresie [{a},{b}] jest {liczb_pierwszych(a,b)} liczb pierwszych")
    return

def liczb_pierwszych(a,b):
    licznik=0
    for i in range (a,b+1):
        if czy_pierwsza(i)==1:
            licznik+=1
    return licznik




import math
def czy_pierwsza(x):
    pierwiastek=int(math.sqrt(x)+1)
    wynik=1
    for i in range (2,pierwiastek+1):
        if x%i==0:
            wynik=0
            break
    return wynik

'''
def kolejnosc_dwoch(a,b):
    if a>b:
        c=a
        a=b
        b=c
    return (a,b)
'''
if __name__ =='__main__':
    main()
