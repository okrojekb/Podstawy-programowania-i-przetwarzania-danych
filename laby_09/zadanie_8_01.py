import numpy
from PIL import Image
import math

def main():
    A=png_read("skimage_astronaut.png")
    png_write(A, "output.png")
    #print(f"macierz a: {A}")
    #mini, maks = maks_i_min(A)
    #print(f"minimalny element to: {mini}, a maksymalny to: {maks}")
    #print(f"rozjasniona macierz to: ")
    b=10
    #rozjasnienie(A, b)
    #negatyw(A)
    #czarno_bialy(A, b)
    #rozciaganie_kontrastu(A,b)
    C=[[1,2,3],[2,3,4],[3,4,5],[4,5,6],[5,6,7],[4,8,3]]
    B=[[0,-1,0],[-1,5,-1],[0,-1,0]]
    D=[[1,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,0],[0,0,0,0,1]]
    E=[[-1,-1,-1],[-1,4,-1],[-1,-1,-1]]
    #png_write(A, "output.png")
    a = convolution(A, E)
    print(f"macierz w to {a}")
    png_write(a, "output.png")

    return


def png_read(filepath):
    img = Image.open(filepath)
    assert len(img.size)==2 # skala szarosci, nie RGB
    return (numpy.array(img)/255).reshape(img.size[1], img.size[0]).tolist()

def png_write(img, filepath):
    img = Image.fromarray((numpy.array(img)*255).astype(numpy.int8), 'L')
    img.save(filepath)

def maks_i_min(macierz_A):
    mini=float("inf")
    maks=float("-inf")
    n=len(macierz_A)
    m=len(macierz_A[0])
    for i in range(n):
        for j in range(m):
            elem=macierz_A[i][j]
            if elem<mini:
                mini=elem
            if elem>maks:
                maks=elem
    return mini, maks

def rozjasnienie(macierz_A, b):
    n = len(macierz_A)
    m = len(macierz_A[0])
    for i in range(n):
        for j in range(m):
            elem=macierz_A[i][j]+b
            if elem>1:
                elem=1
            if elem<0:
                elem=0
            macierz_A[i][j]=elem
    return macierz_A

def negatyw(macierz_A):
    n = len(macierz_A)
    m = len(macierz_A[0])
    for i in range(n):
        for j in range(m):
            macierz_A[i][j] = 1 - macierz_A[i][j]
    return macierz_A

def czarno_bialy(macierz_A, p):
    n = len(macierz_A)
    m = len(macierz_A[0])
    for i in range(n):
        for j in range(m):
            elem=macierz_A[i][j]
            if elem>p:
                elem=1
            else:
                elem=0
            macierz_A[i][j]=elem
    return macierz_A

def rozciaganie_kontrastu(macierz_A, q):
    n = len(macierz_A)
    m = len(macierz_A[0])
    for i in range(n):
        for j in range(m):
            c = macierz_A[i][j]
            elem=1/(1+(math.exp(-q*(c-0.5))))
            macierz_A[i][j]=elem
    return macierz_A

def convolution(macierz_A, macierz_B):
    n = len(macierz_A)
    m = len(macierz_A[0])
    macierz_W=[None for a in range(n)]
    k=len(macierz_B)
    roznica=k//2
    for i in range(n):
        wierszW=[None for z in range(m)]
        if i < roznica:
            do_gory = -i
        else:
            do_gory = -roznica
        if n - 1 - i < roznica:
            do_dolu = n - 1 - i
        else:
            do_dolu = roznica
        for j in range(m):
            if j < roznica:
                do_lewej = -j
            else:
                do_lewej = -roznica
            if m - 1 - j < roznica:
                do_prawej = m - 1 - j
            else:
                do_prawej = roznica
            mini_A=[None for i in range(do_dolu-do_gory+1)]
            mini_B=[None for i in range(do_dolu-do_gory+1)]
            for d in range(len(mini_A)):
                wiersz_A=[None for i in range(-do_lewej+do_prawej+1)]
                wiersz_B=[None for i in range(-do_lewej+do_prawej+1)]
                dodac_wiersze = do_gory
                dodac_kolumny = do_lewej
                for l in range(len(wiersz_A)):

                    #for f in range(do_gory,do_dolu+1):
                        #for e in range(do_lewej,do_prawej+1):
                    elem_A=macierz_A[i+dodac_wiersze+d][j+dodac_kolumny+l]
                    elem_B=macierz_B[roznica+dodac_wiersze+d][roznica+dodac_kolumny+l]
                    #dodac_wiersze+=1
                    #dodac_kolumny+=1

                    wiersz_A[l]=elem_A
                    wiersz_B[l]=elem_B
                mini_A[d]=wiersz_A
                mini_B[d]=wiersz_B
            suma=0
            for d in range(len(mini_A)):
                wierszA = mini_A[d]
                wierszB = mini_B[d]
                for l in range(len(wierszA)):
                    elemA=wierszA[l]
                    elemB=wierszB[l]
                    suma+=elemB*elemA
            wierszW[j]=suma
        macierz_W[i]=wierszW
    return macierz_W

if __name__ == '__main__':
    main()