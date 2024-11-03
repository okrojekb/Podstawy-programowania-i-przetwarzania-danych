def main():
    n = int(input("Podaj dodatnia liczbe naturalna: "))
    if n<=0:
        raise Exception("Liczba miala byc dodatnia!")
    m = n
    krok = 0
    niezerowe_n = 0
    licznik_niezerowy = 0
    while n>=10:
        krok+=1
        iloczyn = 1
        liczba_cyfr = 0
        while n>=(10**liczba_cyfr):
            liczba_cyfr+=1
        #print(f"liczba cyfr toL {liczba_cyfr}")
        for i in range(1, liczba_cyfr+1):
            cyfra = n%10
            #print(f"cyfra; {cyfra}")
            if cyfra!=0:
                iloczyn*=cyfra
                #print(f"iloczyn: {iloczyn}")
                if krok==1:
                    niezerowe_n+=(cyfra*(10**licznik_niezerowy))
                    licznik_niezerowy+=1
                #print(f"niezerowe n: {niezerowe_n}")
            n = n//10
            #print(f"nowe n: {n}")
        n = iloczyn
    indeks = n
    print(f"Po pominięciu wszystkich zer w zapisie dziesiętnym liczby {m} otrzymamy liczbe {niezerowe_n}.")
    print(f"Indeks numerologiczny liczby {m} wynosi {indeks}.")
    print(f"Jestesmy w stanie go obliczyc w {krok} krokach.")
    return










if __name__ == '__main__':
        main()
