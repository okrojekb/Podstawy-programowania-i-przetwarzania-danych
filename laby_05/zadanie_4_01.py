'''
laby nr 4
zadanie 1
'''

def main():
    s=int(input("Podaj ziarno generatora: "))
    n = int(input("Podaj liczbe wartosci do wygenerowania: "))
    print(f"liczby pseudolosowe to: \n{generator_pseudolosowych(s,n)}")
    return

def generator_pseudolosowych(s, n):

    with open("plik.txt", "w") as plik_1:
        plik_1.write("")
    m = (2**31)-1
    a = 1103515245
    c = 12345
    for i in range(n):
        s=(a*s + c)%m
        with open("plik.txt", "a") as plik_1:
            plik_1.write(f"{s/m} \n")

    with open("plik.txt", "r") as plik_1:
        wynik=plik_1.read()
    return wynik


if __name__ == '__main__':
    main()