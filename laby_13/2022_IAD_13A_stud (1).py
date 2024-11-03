import random

class Turtle:
    __slots__ = ["position", "min_position", "max_position", "identifier"]

    def __init__(self, identifier, position, min_position, max_position):
        self.position = position
        self.min_position = min_position
        self.max_position = max_position
        self.identifier = identifier

    def __str__(self):
        return f'{self.identifier}'

    def make_move(self):

        los = random.random()
        indx=self.position[0]
        indy=self.position[1]

        if los < 0.4:
            indx+=1
        elif los < 0.8:
            indy+=1
        elif los < 0.88:
            indx-=1
        elif los < 0.96:
            indy-=1

        if indx <= self.max_position[0] and indx >= 0 and indy <=self.max_position[1] and indy >= 0:
            self.position = (indx, indy)

        #
        # napis+=f"zolw nr{self.indenti }"
        # if los < 0.4 and indx + 1 <= self.max_position[0]:
        #     self.position = (indx + 1,indy)
        # elif los < 0.8 and indy + 1 <= self.max_position[1]:
        #     self.position = (indx, indy + 1)
        # elif los < 0.88 and indx - 1 >= self.min_position[0]:
        #     self.position = (indx - 1, indy)
        # elif los < 0.96 and indy - 1 >= self.min_position[1]:
        #     self.position = (indx, indy - 1)
        return self


    def has_finished(self):
        if self.position == self.max_position:
            return True
        else:
            return False

    def __repr__(self):
        return f"Zolw=(position={self.position}, min_position={self.min_position}, max_position={self.max_position}, indentifier={self.identifier}"


class Board:
    __slots__ = ["board_size", "turtles"]
    '''
    def __init__(self, board_size):
        self.board_size=int(board_size)
        mozliwe_starty=[]
        for i in range(board_size):
            for j in range(board_size-i):
                mozliwe_starty.append((i,j))
        ilosc_zolwi=int(0.1*board_size*board_size)
        minimalna_pozycja=(0,0)
        maksymalna_pozycja=(board_size-1, board_size-1)
        turtles=[]
        ilosc_pozycji=len(mozliwe_starty)
        for i in range(ilosc_zolwi):
            identyfikator=i+1
            los=random.randint(0,ilosc_pozycji-1-i)
            pozycja_startowa=mozliwe_starty.pop(los)
            zolw=Turtle(identyfikator, pozycja_startowa, minimalna_pozycja, maksymalna_pozycja)
            turtles.append(zolw)
        self.turtles=turtles

    def __init__(self, board_size):
        self.board_size = int(board_size)
        turtles=[]
        ilosc_zolwi=int(0.1*board_size*board_size)
        minimalna_pozycja = (0, 0)
        maksymalna_pozycja = (board_size - 1, board_size - 1)
        for i in range(ilosc_zolwi):
            identyfikator = i + 1
            x = random.randint(0, board_size - 1)
            y = random.randint(0, board_size - 1 - x)
            pozycja_startowa=(x,y)
            zolw = Turtle(identyfikator, pozycja_startowa, minimalna_pozycja, maksymalna_pozycja)
            turtles.append(zolw)
        self.turtles = turtles
'''

    def __init__(self, board_size):
        self.board_size = int(board_size)
        turtles = []
        ilosc_zolwi = int(0.1 * board_size * board_size)
        minimalna_pozycja = (0, 0)
        maksymalna_pozycja = (board_size - 1, board_size - 1)

        pozycje_startowe = []
        for i in range(ilosc_zolwi):
            identyfikator = i + 1
            nie_powtarza = 1
            while nie_powtarza > 0:
                nie_powtarza=1
                x = random.randint(0, board_size - 1)
                y = random.randint(0, board_size - 1 - x)
                pozycja_zolwia = (x, y)
                for i in pozycje_startowe:
                    if i == pozycja_zolwia:
                        nie_powtarza = 2
                        break
                if nie_powtarza == 1:
                    nie_powtarza = 0
            pozycje_startowe.append(pozycja_zolwia)
            zolw = Turtle(identyfikator, pozycja_zolwia, minimalna_pozycja, maksymalna_pozycja)
            turtles.append(zolw)
        self.turtles = turtles



    def __str__(self):
        board_matrix = self.create_matrix()
        board_printing = ''
        for j in range(len(board_matrix[0])*2 + 2):
            board_printing += "-"

        board_printing += '\n'

        for i in range(len(board_matrix)):
            board_printing+= "|"
            for j in range(len(board_matrix[i])):
                if board_matrix[i][j] is not None:
                    board_printing += f'{board_matrix[i][j]:2d}'
                else:
                    board_printing+= "  "
            board_printing+= "|\n"

        for j in range(len(board_matrix[0])*2 + 2):
            board_printing+='-'
        board_printing+='\n'

        return board_printing

    def create_matrix(self):
        macierz=[[] for i in range(self.board_size)]
        for i in range(self.board_size):
            for j in range(self.board_size):
                macierz[i].append(None)
        turtles=self.turtles
        for i in range(len(turtles)):
            indeksx=turtles[i].position[0]
            indeksy=turtles[i].position[1]
            if macierz[indeksx][indeksy]==None:
                macierz[indeksx][indeksy]=turtles[i].identifier
            else:
                macierz[indeksx][indeksy]+=turtles[i].identifier
        return macierz

    def is_over(self):
        for i in self.turtles:
            if not i.has_finished():
                return False
        return True
    
    def next_round(self):
        for i in self.turtles:
            i.make_move()
        return self


def main():
    #random.seed(2022)
    board_size=int(input("Please provide board size: "))
    plansza=Board(board_size)
    print(plansza)
    print(plansza.turtles)
    ile=0
    while not plansza.is_over():
        plansza.next_round()
        print(plansza)
        ile+=1
    print(ile)




if __name__ == '__main__':
    main()