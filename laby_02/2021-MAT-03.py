"""
PPiPD laby 1 zadanie nr 3
Laby Zadanie nr 1.3 py
"""
def main():
    decyzja=0
    while decyzja ==0:
        print("Co chcesz zrobić?")
        print("0 - Sprawdzic czy dwie liczby sa lustrzane")
        print("1 - Zakonczyc")
        decyzja = int(input("Podaj '0' albo '1': "))
        if decyzja == 1:
            continue
        elif decyzja>1:
            print("Bledny wybor. Sprobuj jeszcze")
            decyzja=0
            continue
        print("Podaj dwie liczby z zakresu [1, 10^10]")
        liczba_a=int(input("Podaj pierwsza liczbe: "))
        liczba_b=int(input("Podaj druga liczbe: "))
        if (10**10)<liczba_b or liczba_b<1 or (10**10)<liczba_a or liczba_a<1:
            raise ValueError("Liczby musza byc dodatnie i mniejsze od 10^10.")
        iloraz =max(liczba_b, liczba_a)/min(liczba_b, liczba_a)
        if iloraz>=10:
            print("Liczby maja rozna liczbe cyfr.")
            print("Nie moga to byc liczby lustrzane.")
            decyzja=1
            continue
        print("Liczby maja taka sama liczbe cyfr")
        liczba_cyfr=0
        while 10**liczba_cyfr<=liczba_a:
            liczba_cyfr+=1
        for i in range(1,liczba_cyfr+1):
            if liczba_a%10!=liczba_b//(10**(liczba_cyfr-i)):
                print("Podane liczby NIE sa liczbami lustrzanymi")
                break
            liczba_a=liczba_a//10
            liczba_b=liczba_b%(10**(liczba_cyfr-i))
            #print(f"a: {liczba_a}, b: {liczba_b}.")
        if liczba_a==liczba_b==0:
            print("Podane liczby SA liczbami lustrzanymi.")

    return



if __name__ == '__main__':
        main()
