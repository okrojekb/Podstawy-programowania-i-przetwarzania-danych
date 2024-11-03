import math
def main():
    n=int(input("Podaj liczbe calkowita wieksza niz 1: "))
    if n<=1:
        raise Exception("Liczba miala byc wieksza niz 1!")
    dzielnik = 2
    print(f"Dzielniki pierwsze liczby {n} to: ")
    liczba_bez_krotnosci = 1
    max_krotnosc = 0
    m = n
    dzielnik_z_max_krotnoscia = 0
    while n>1:
        krotnosc = 0
        if n%dzielnik==0:
            print(f"{dzielnik}")
            liczba_bez_krotnosci*=dzielnik
            while n%dzielnik==0:
                krotnosc+=1
                n=n/dzielnik
                #print(f"n to :{n}")
            if krotnosc>max_krotnosc:
                max_krotnosc=krotnosc
                dzielnik_z_max_krotnoscia=dzielnik
        dzielnik+=1
    print(f"W rozkladzie {m} na czynniki pierwsze najczesciej pojawia sie {dzielnik_z_max_krotnoscia}, wystepuje {max_krotnosc} razy.")
    print(f"Jezeli w rozkladzie {m} na czynniki pierwsze pominiemy krotnosci, otrzymamy liczbe {liczba_bez_krotnosci}.")
    return














if __name__ == '__main__':
        main()