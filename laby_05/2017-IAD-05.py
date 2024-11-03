'''
laby nr 4
zadanie 1
'''


def main():
    with open("input.txt", "r") as plik_wejsciowy:
        a_1 = float(plik_wejsciowy.readline())
        a_n = float(plik_wejsciowy.readline())
        n = int(plik_wejsciowy.readline())
        b_1 = float(plik_wejsciowy.readline())
        b_m = float(plik_wejsciowy.readline())
        m = int(plik_wejsciowy.readline())
    f_min = float("inf")
    f_max = float("-inf")
    a_max = float("-inf")
    b_max = float("-inf")

    if a_1 >= a_n or b_1 >= b_m or m <= 0 or n <= 0:
        raise ValueError("Bledne dane")
    r_a = ((a_n - a_1) / (n - 1))
    r_b = ((b_m - b_1) / (m - 1))

    with open("output.txt", "w") as plik_wyjsciowy:
        for a in range(-2, n):
            a_i = a_1 + a * r_a
            if a == -1:
                for i in range((m * 7) - 2):
                    if i == 6:
                        plik_wyjsciowy.write('|')
                    else:
                        plik_wyjsciowy.write('_')
                print("", file=plik_wyjsciowy)
                continue

            for b in range(-2, m):
                b_i = b_1 + b * r_b

                if a == -2 and b == -2:
                    plik_wyjsciowy.write(f"{'a / b':<6s}")
                elif b == -1:
                    plik_wyjsciowy.write(f"{'|':^1s}")
                elif a == -2:
                    plik_wyjsciowy.write(f"{b_i:^6.2f}")
                elif b == -2:
                    plik_wyjsciowy.write(f"{a_i:<6.1f}")
                else:
                    plik_wyjsciowy.write(f"{F(a_i, b_i):^6.2f}")
                    wartoscf = F(a_i, b_i)
                    if wartoscf > f_max:
                        f_max = wartoscf
                        a_max = a_i
                        b_max = b_i
                    if wartoscf < f_min:
                        f_min = wartoscf
            print("", file=plik_wyjsciowy)
    print(
        f"Wartości minimalna funkcji to: {f_min}, a wartosc maksymalna funkcji to {f_max} i jest ona osiągnięta dla a= {a_max} i b= {b_max}.")

    import matplotlib.pyplot as plt
    import matplotlib.patches as patches
    fig = plt.figure()
    ax = fig.add_subplot(111)
    # ustal zakresy na osiach:
    ax.set_xlim([(a_1 - (r_a / 2)), (a_n + (r_a / 2))])  # zakres wartości na osi OX [xmin, xmax]
    ax.set_ylim([(b_1 - (r_b / 2)), (b_m + (r_b / 2))])  # zakres wartości na osi OY [ymin, ymax]
    # przykładowy jasnoszary prostokąt o wierzchołkach (0.1, 0.5) i (0.6, 2.75):
    for a in range(n):
        a_i = (a_1 + a * r_a)
        for b in range(m):
            b_i = (b_1 + b * r_b)
            ax.add_patch(patches.Rectangle(
                ((a_i - (r_a / 2)), (b_i - (r_b / 2))),  # (x,y)
                r_a,  # szerokosc
                r_b,  # wysokosc
                facecolor=str((F(a_i, b_i) - f_min) / (f_max - f_min))  # stopien szarosci (od 0 do 1) jako napis
            ))
            # ax.add_patch(patches.Rectangle(....)) można będziemy wywoływać wielokrotnie
            # zapis do PNG po zakończeniu rysowania
            fig.savefig('output.png', dpi=90)

    return


import numpy as np
from sklearn import datasets, svm


def F(a, b):
    '''
    Nie interesuje nas, co funkcja robi:
    traktujemy ja jako "czarna skrzynke".
    Wazne jest jedynie to, ze F(a, b) zwraca wartość z przedzialu [0,1]
    dla a, b > 0
    Przykład inspirowany http://scikit-learn.org/stable/auto_examples/
    exercises/plot_iris_exercise.html
    '''
    iris = datasets.load_iris()  # zbior iris
    X, y = iris.data, iris.target
    X, y = X[y != 0, :2], y[y != 0]  # tylko klasy 1 i 2
    n_sample = len(X)
    np.random.seed(1234)
    order = np.random.permutation(n_sample)
    X = X[order]
    y = y[order].astype(float)
    X_train = X[:int(0.8 * n_sample)]  # proba uczaca = losowe 80%
    y_train = y[:int(0.8 * n_sample)]
    X_test = X[int(0.8 * n_sample):]  # proba testowa = pozostale 20%
    y_test = y[int(0.8 * n_sample):]
    clf = svm.SVC(gamma=a, C=b)  # support vector classifier
    clf.fit(X_train, y_train)
    return np.mean(clf.predict(X_test) == y_test)  # accuracy, wartość z [0,1]


if __name__ == '__main__':
    main()
