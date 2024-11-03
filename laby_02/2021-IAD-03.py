"""
PPiPD laby 1 zadanie nr 3
Laby Zadanie nr 1.3 py
"""
def main():
   wysokosc = int(input("Podaj wysokość pomieszczenia (wybierz: 7, 9, 11): "))
   szerokosc = 10
   wysokosc_okna = 3
   szerokosc_okna = 3
   if not (wysokosc==7 or wysokosc==9 or wysokosc==11):
       raise ValueError("Bledne dane")
   x_rozmiar = int(input("Podaj dlugosc rolki x: "))
   o_rozmiar = int(input("Podaj dlugosc rolki o: "))
   czas_przyklejenia_jednoski_x = float(input("podaj czas przyklejenia jednej jednoski tapety x: "))
   czas_przyklejenia_jednoski_o = czas_przyklejenia_jednoski_x/3
   if x_rozmiar<=0 or o_rozmiar<=0:
       raise ValueError("bledne dane)")
   if x_rozmiar>(szerokosc-1) or o_rozmiar>(x_rozmiar/2):
       raise ValueError("bledne dane")
   czas_tapetowania =0
   czas_zmiany_rolki =3*czas_przyklejenia_jednoski_x
   rzad_poczatku_okna = wysokosc-(wysokosc_okna+2)
   kolumna_poczatku_okna = szerokosc-(szerokosc_okna+2)
   licznik=0
   ilosc_rolek_o =0
   ilosc_rolek_x =0
   suma = x_rozmiar + o_rozmiar
   for wiersz in range(wysokosc):
       for kolumna in range(szerokosc):
           if (((rzad_poczatku_okna)<=wiersz<(rzad_poczatku_okna+3)) and (kolumna_poczatku_okna<=kolumna<(kolumna_poczatku_okna+3))):
               print(" ", end = "")
               continue
           elif 0<=(licznik%suma)<o_rozmiar:
                print("o", end = "")
                licznik+=1
                ilosc_rolek_o+=1
                czas_tapetowania+=czas_przyklejenia_jednoski_o

           else:
               print("x", end = "")
               licznik+=1
               ilosc_rolek_x+=1
               czas_tapetowania+=czas_przyklejenia_jednoski_x

       print("")
   if ilosc_rolek_x%x_rozmiar==0:
       ilosc_rolek_x=ilosc_rolek_x//x_rozmiar
   else:
       ilosc_rolek_x=(ilosc_rolek_x//x_rozmiar)+1
   if ilosc_rolek_o%o_rozmiar==0:
       ilosc_rolek_o=ilosc_rolek_o//o_rozmiar
   else:
       ilosc_rolek_o=(ilosc_rolek_o//o_rozmiar)+1
   czas_tapetowania = czas_tapetowania + (czas_zmiany_rolki*(ilosc_rolek_o+ilosc_rolek_x))
   print(f"Wytapetowanie calego pokoju zajelo {czas_tapetowania} jednostek czasu")
   print(f"Podczas tapetowania zuzyto: {ilosc_rolek_x} rolek x i {ilosc_rolek_o} rolek tapety o.")


if __name__ == '__main__':
        main()
