def main():
    liczba_graczy = int(input("POdaj liczbe graczy (>=2): "))
    liczba_talii = int(input("Podaj liczbe dostepnych talii (>=1): "))
    if liczba_talii<1 or liczba_graczy<2:
        raise ValueError("Bledne dane")
    potrzebne_karty = (liczba_graczy*5)+1
    max_graczy=0
    if potrzebne_karty%52==0:
        potrzebne_talie = potrzebne_karty//52
    else:
        potrzebne_talie = (potrzebne_karty//52)+1
    print(f"Dla {liczba_graczy} graczy potrzebne są {potrzebne_talie} talie.")
    if potrzebne_talie<=liczba_talii:
        dostepne_karty = liczba_talii*52
        max_graczy = (dostepne_karty-1)//5
        print(f"Do gry z {liczba_talii} mogloby dolaczyc maksymalnie {max_graczy}.")
    return










if __name__ == '__main__':
    main()