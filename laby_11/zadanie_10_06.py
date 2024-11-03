def main():
    lista1=[1,3,5,6,3]
    lista2=[2,3,1,5,5,4]
    print(merge(lista1, lista2))
    lista3=[1,3,3,5,6]
    lista4=[1,2,3,4,5,5]
    print(merge_sorted(lista3,lista4))



def merge(x,y):
    n=len(x)
    m=len(y)
    u=[]
    v=[]
    wynik=[]
    for i in range(n):
        elem=x[i]
        for j in range(m):
            if elem==y[j]:
                u.append(i)
                v.append(j)
    return [u,v]

def merge_sorted(x,y):
    n = len(x)
    m = len(y)
    u = []
    v = []
    wynik = []
    for i in range(n):
        elem = x[i]
        licznik=0
        for j in range(licznik,m):
            if elem==y[j]:
                u.append(i)
                v.append(j)
            if elem<y[j]:
                licznik=j-1
                break
    return [u,v]

if __name__ == '__main__':
        main()