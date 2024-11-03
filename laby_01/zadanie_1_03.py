"""
PPiPD laby 1 zadanie nr 3
Laby Zadanie nr 1.3 py
"""
def main():
    print("Podaj kolejne wspolczynniki pierwszego rownania wedlug wzoru: a*x+b*y=c")
    a = float(input("Podaj wspolczynnik a: "))
    b = float(input("Podaj wspolczynnik b: "))
    c = float(input("Podaj wspolczynnik c: "))
    print("podaj kolejne wspolczynniki drugiego rownania wedlug wzoru: d*x+e*y=f")
    d = float(input("Podaj wspolczynnik d: "))
    e = float(input("Podaj wspolczynnik e: "))
    f = float(input("Podaj wspolczynnik f: "))
    typ_ukladu =Typ_ukladu(a,b,c,d,e,f)
    print(f"Ten uklad rownan jest {typ_ukladu}.")
    if typ_ukladu=="nieoznaczony":
        print("Ten uklad rownan ma nieskonczenie wiele rozwiazan.")
    elif typ_ukladu=="sprzeczny":
        print("Ten uklad rownan nie ma rozwiazan.")
    else:
        rozwiazanie=Szukanie_rozwiazania(a,b,c,d,e,f)
        print(f"Rozwiazaniem tego ukladu rownan jest: x={rozwiazanie[0]} i y={rozwiazanie[1]}.")
    return

def Liczenie_W (a,b,d,e):
    W=a*e-b*d
    return W

def Licznie_Wx (b,c,e,f):
    Wx=c*e-b*f
    return Wx

def Liczenie_Wy (a,c,d,f):
    Wy=a*f-c*d
    return Wy

def Typ_ukladu (a,b,c,d,e,f):
    W=Liczenie_W(a,b,d,e)
    Wx=Licznie_Wx(b,c,e,f)
    Wy=Liczenie_Wy(a,c,d,f)
    if W==Wx and W==Wy and W==0:
        wynik="nieoznaczony"
    elif W==0 and (Wx!=0 or Wy!=0):
        wynik="sprzeczny"
    else:
        wynik = "oznaczony"
    return wynik

def Szukanie_rozwiazania(a,b,c,d,e,f):
    W = Liczenie_W(a, b, d, e)
    Wx = Licznie_Wx(b, c, e, f)
    Wy = Liczenie_Wy(a, c, d, f)
    x=Wx/W
    y=Wy/W
    return (x,y)

if __name__ == '__main__':
        main()
