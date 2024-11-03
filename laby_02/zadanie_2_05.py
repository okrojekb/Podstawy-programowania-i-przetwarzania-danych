"""
PPiPD zajęcia drugie
zadanie 2.06 py
"""

def main():
    k=float(input("Podaj k: "))

    if k!=int(k):
        raise ValueError("K musi byc liczba calkowita")
    if k<=0:
        raise ValueError("K musi byc wieksze od 0")
    k=int(k)
    #y = int(input("Podaj y: "))
    x = min_k_elementow(k)
    #print(f"ilosc elementow ciagu: {ilosc_elementow(x)}")
    #print(f"ilosc elementow ciagu dla y: {ilosc_elementow(y)}")
    print(f"minimalne x to: {min_k_elementow(k)}")
    return

def element_parzysty(x):
    y=x/2
    return y

def element_nieparzysty(x):
    y=3*x+1
    return y

def ilosc_elementow(x):
    licznik=1
    while x!=1:
        if x%2==0:
            x=element_parzysty(x)
        else:
            x=element_nieparzysty(x)
        licznik+=1
        #print(f"x={x} i licznik={licznik}")
    return licznik

def min_k_elementow(k):
    x=1
    while True:
        licznik=ilosc_elementow(x)
        if licznik<k:
            x+=1
            #print("nowe x")
        else:
            break
    return x

if __name__ =='__main__':
    main()
