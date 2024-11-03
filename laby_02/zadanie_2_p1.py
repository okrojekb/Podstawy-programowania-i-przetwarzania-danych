import math
def main():
    rok_u = int(input("Podaj rok urodzenia: "))
    if rok_u<1900:
        raise ValueError("Bledne dane")
    miesiac_u = int(input("Podaj miesiac urodzenia: "))
    if 1>miesiac_u or miesiac_u>12:
        raise ValueError("Bledne dane")
    dzien_u = int(input("Podaj dzien urodzenia: "))
    if 1>dzien_u or dzien_u>31:
        raise ValueError("Bledne dane")
    if miesiac_u == 4 or miesiac_u == 6 or miesiac_u == 9 or miesiac_u == 11:
        if dzien_u==31:
            raise ValueError("Bledne dane")
    if miesiac_u == 2:
        if dzien_u>29:
            raise ValueError("Bledne dane")
        if not((rok_u%4==0 and rok_u%100!=0) or rok_u%400==0):
            if dzien_u==29:
                raise ValueError("Bledne dane")

    rok_t = int(input("Podaj rok referencyjne: "))
    if rok_t < 1900 or rok_u>rok_t:
        raise ValueError("Bledne dane")
    miesiac_t = int(input("Podaj miesiac referencyjny: "))
    if 1 > miesiac_t or miesiac_t > 12:
        raise ValueError("Bledne dane")
    dzien_t = int(input("Podaj dzien referencyjny: "))
    if 1 > dzien_t or dzien_t > 31:
        raise ValueError("Bledne dane")
    if miesiac_t == 4 or miesiac_t == 6 or miesiac_t == 9 or miesiac_t == 11:
        if dzien_t == 31:
            raise ValueError("Bledne dane")
    if miesiac_t == 2:
        if dzien_t > 29:
            raise ValueError("Bledne dane")
        if not ((rok_t % 4 == 0 and rok_t % 100 != 0) or rok_t % 400 == 0):
            if dzien_t == 29:
                raise ValueError("Bledne dane")
    if rok_t==rok_u:
        if miesiac_u>miesiac_t:
            raise ValueError("Bledne dane")
        elif miesiac_u==miesiac_t:
            if dzien_u>=dzien_t:
                raise ValueError("Bledne dane")

    if miesiac_u==3:
        if dzien_u<21:
            print("Urodziles sie w zimie")
        else:
            print("Urodziles sie w wiosne")
    if miesiac_u==4 or miesiac_u==5:
        print("Urodziles sie w wiosne")
    if miesiac_u == 6:
        if dzien_u<22:
            print("Urodziles sie w wiosne")
        else:
            print("Urodziles sie w lato")
    if miesiac_u==7 or miesiac_u==8:
        print("Urodziles sie w lato")
    if miesiac_u==9:
        if dzien_u<23:
            print("Urodziles sie w lato")
        else:
            print("Urodziles sie w jesien")
    if miesiac_u==10 or miesiac_u==11:
        print("Urodziles sie w wiosne")
    if miesiac_u==12:
        if dzien_u<22:
            print("Urodziles sie w jesien")
        else:
            print("Urodziles sie w zime")
    if miesiac_u==1 or miesiac_u==2:
        print("Urodziles sie w zime")

    if miesiac_u==1 or miesiac_u==2:
        Y=rok_u-1
    else:
        Y=rok_u

    y=Y%100
    c=Y//100
    m=miesiac_u-2
    if miesiac_u==1:
        m=11
    if miesiac_u==2:
        m=12
    dzien_tygodnia = (dzien_u + (((2.6*m)-0.2)//1) + y + (y//4) + (c//4) - (2*c))%7

    if dzien_tygodnia==5:
        wynik="piatek"
    if dzien_tygodnia==6:
        wynik="sobota"
    if dzien_tygodnia==0:
        wynik="niedziela"
    if dzien_tygodnia==1:
        wynik="poniedzialek"
    if dzien_tygodnia==2:
        wynik="wtorek"
    if dzien_tygodnia==3:
        wynik="sroda"
    if dzien_tygodnia==4:
        wynik="czwartek"
    print(f"Był to {wynik}.")
    if rok_t==rok_u:
        wiek_l=0
        if miesiac_u==miesiac_t:
            wiek_m=0
            wiek_d = dzien_t - dzien_u
    else:
        if miesiac_u < miesiac_t:
            wiek_l=rok_t-rok_u
            if dzien_u<=dzien_t:
                wiek_m=miesiac_t-miesiac_u
                wiek_d=dzien_t-dzien_u
            else:
                wiek_m=miesiac_t-miesiac_u-1
                wiek_d=dzien_t
                if miesiac_t-1 == 4 or miesiac_t-1 == 6 or miesiac_t-1 == 9 or miesiac_t-1 == 11:
                    wiek_d+=(30-dzien_u)
                if miesiac_t-1 == 2:
                    if not ((rok_u % 4 == 0 and rok_u % 100 != 0) or rok_u % 400 == 0):
                        wiek_d+=(28-dzien_u)
                    else:
                        wiek_d+=(29-dzien_u)
        elif miesiac_t==miesiac_u:
            if dzien_u<=dzien_t:
                wiek_l=rok_t-rok_u
                wiek_m=0
                wiek_d=dzien_t-dzien_u
            else:
                wiek_l=rok_t-rok_u-1
                wiek_m=11
                wiek_d=dzien_t
                if miesiac_t-1 == 4 or miesiac_t-1 == 6 or miesiac_t-1 == 9 or miesiac_t-1 == 11:
                    wiek_d+=(30-dzien_u)
                if miesiac_t-1 == 2:
                    if not ((rok_u % 4 == 0 and rok_u % 100 != 0) or rok_u % 400 == 0):
                        wiek_d+=(28-dzien_u)
                    else:
                        wiek_d+=(29-dzien_u)
        else:
            wiek_l=rok_t-rok_u-1
            if dzien_u<=dzien_t:
                wiek_m=miesiac_t+(12-miesiac_u)
                wiek_d=dzien_t-dzien_u
            else:
                wiek_m=miesiac_t+(11-miesiac_u)
                wiek_d=dzien_t
                if miesiac_t-1 == 4 or miesiac_t-1 == 6 or miesiac_t-1 == 9 or miesiac_t-1 == 11:
                    wiek_d+=(30-dzien_u)
                if miesiac_t-1 == 2:
                    if not ((rok_u % 4 == 0 and rok_u % 100 != 0) or rok_u % 400 == 0):
                        wiek_d+=(28-dzien_u)
                    else:
                        wiek_d+=(29-dzien_u)
    print(f"Masz {wiek_l} lat, {wiek_m} miesiecy i {wiek_d} dni.")
    return




if __name__ == '__main__':
    main()