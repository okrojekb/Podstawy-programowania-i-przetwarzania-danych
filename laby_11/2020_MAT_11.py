

def main():
    N = 40
    przedzialy=[(1,10),(12,30),(15,25),(26,29),(7,21),(32,38)]
    wypisz_przedzialy([(1,10),(12,30),(15,25),(26,29),(7,21),(32,38)])
    skurczone_przedialy=skurcz(przedzialy,2,3)
    wypisz_przedzialy(skurczone_przedialy)
    #p1=(5,10)
    #p2=(13,15)
    for i in range(len(przedzialy)):
        p1=p1=(5,10)
        p2=przedzialy[i]
        print(f"odleglosc{p1}, {p2}) == {odleglosc(p1,p2)}")
    #wynik = odleglosc(p1,p2)
    #print(f"odleglosc{p1}, {p2}) == {wynik}")
    bliskie=znajdz_bliskie(przedzialy,3)
    print(bliskie)


def wypisz_os(x_max, krok):
    print('0', end='')
    i = krok
    while i <= x_max:
        print(f'{i:.>{krok}d}', end='')
        i += krok
    print('.' * (x_max - i))

def wypisz_przedzialy(przedzialy, x_max=40, krok=5):
    assert isinstance(przedzialy, list), "Podany obiekt nie jest listą."
    wypisz_os(x_max, krok)
    for i in range(len(przedzialy)):
        elem=przedzialy[i]
        a=len(elem)

        if not (isinstance(przedzialy[i], tuple) or isinstance(przedzialy[i], list)):
            print(f'Przedział {i} nie jest listą/krotką.')
        elif len(przedzialy[i]) !=2:
            print(f'Przedział {i} nie ma długości 2.')
        elif not (0 <= przedzialy[i][0] < przedzialy[i][1] <= x_max):
            print(f'Nieprawidłowe końce przedziału: "{przedzialy[i]}"')
        else:
            a, b = przedzialy[i]
            print(' ' * a + '#' * (b - a + 1) + ' ' * (x_max - b), end='')
            print(f' [{a:2d}, {b:2d}], dlugosc={b - a + 1}')

def skurcz(przedzialy, k, d):
    wynik=[]
    for i in przedzialy:
        dlugosc=i[1]-i[0]+1
        if dlugosc-2*k<d:
            continue
        nowy_przedzial=(i[0]+k,i[1]-k)
        wynik.append(nowy_przedzial)
    return wynik

def odleglosc(p1,p2):
    if p1[1]>=p2[0]:
        wynik=0
    else:
        wynik=p2[0]-p1[1]
    return wynik

def znajdz_bliskie(przedzialy, k):
    wynik=[]
    for i in range(len(przedzialy)):
        for j in range(len(przedzialy)):
            roznica=odleglosc(przedzialy[i],przedzialy[j])
            if roznica>0 and roznica<=k:
                wynik.append([przedzialy[i],przedzialy[j], roznica])
                wypisz_przedzialy([przedzialy[i],przedzialy[j]])

    return wynik

if __name__ == '__main__':
        main()