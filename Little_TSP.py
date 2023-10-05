import numpy as np
from numpy import inf


# algorytm Little'a dla problemu TSP
def zmniejsz_i_uzyskaj_lb(macierz):
    redukcja = 0
    # znalezienie najmniejszych wartości w wierszach
    min_wiersz = np.min(macierz, axis=1, keepdims=True)
    # zignorowanie przypadków, gdy znaleziono nieskończoność jako minimum
    min_wiersz[min_wiersz == np.inf] = 0
    # dodanie sumy zmniejszenia wierszy
    redukcja += np.sum(min_wiersz)
    # odjęcie najmniejszych wartości od wierszy
    macierz -= min_wiersz
    # znalezienie najmniejszych wartości w kolumnach
    min_kolumna = np.min(macierz, axis=0)
    # zignorowanie przypadków, gdy znaleziono nieskończoność jako minimum
    min_kolumna[min_kolumna == np.inf] = 0
    # dodanie sumy zmniejszenia kolumn
    redukcja += np.sum(min_kolumna)
    # odjęcie najmniejszych wartości od kolumn
    macierz -= min_kolumna

    return redukcja


def optymistyczny_koszt_zerowych_krawędzi(M):
    # wyszukiwanie indeksów zerowych wartości w macierzy M
    indeksy_zerowych = np.argwhere(M == 0)
    maks_wartość_krawędzi = -np.inf
    maks_indeksy_krawędzi = (None, None)
    # iteracja po zerowych wartościach w macierzy
    for indeks in indeksy_zerowych:
        i, j = indeks
        temp = M[i, j]
        M[i, j] = np.inf
        maks_suma = np.min(M[i, :]) + np.min(M[:, j])
        M[i, j] = temp
        # aktualizacja maksymalnego kosztu krawędzi
        if maks_suma > maks_wartość_krawędzi:
            maks_wartość_krawędzi = maks_suma
            maks_indeksy_krawędzi = [i, j]
    return maks_indeksy_krawędzi


def wykresl_rzad_kolume(macierz, indeksy):
    row, col = indeksy
    # wypelnienie rzedu i kolumny nieskonczonosciami
    for j in range(macierz.shape[0]):
        macierz[row][j] = inf
        macierz[j][col] = inf
    # zabronienie przecinego przejscia
    macierz[col][row] = inf


def little(macierz, najlepsza_suma, suma, rozwiazanie, zbior_rozw=[], rows=0, zabraniam=False):
    if np.all((macierz == inf)):
        # Kryterium zamykania 1 oraz 3. Sprawdzanie czy otrzymaliśmy tyle rozwiązań ile mielismy
        if len(rozwiazanie) == rows:
            # pozbywanie sie duplikatow rozwiazania
            if rozwiazanie not in zbior_rozw:
                zbior_rozw.append(rozwiazanie)
            else:
                return -1
            # Aktualizacja ograniczenia V
            if suma < najlepsza_suma:
                najlepsza_suma = suma
            return najlepsza_suma
        else:
            return -1
    # redukcja macierzy
    suma += zmniejsz_i_uzyskaj_lb(macierz)
    # Kryterium zamykania 2
    if suma > najlepsza_suma:
        return -1
    # wybranie kolejnej ścieżki
    indeksy = optymistyczny_koszt_zerowych_krawędzi(macierz)
    # przypadek z zabranianiem
    if zabraniam:
        row, col = indeksy
        macierz[row][col] = inf
    # przypadek bez zabraniania
    else:
        # wykreslanie
        wykresl_rzad_kolume(macierz, indeksy)
        # dla lepszej wizualizacji inkrementuje o 1 bo python liczy od 0.
        temp = []
        for el in indeksy:
            temp.append(el + 1)
        # dodanie rozwiazania
        rozwiazanie.append(temp)
    # wywolanie rekurencyjne problemu z aktualizajcja ograniczenia
    zmienna1 = little(macierz[:], najlepsza_suma, suma, rozwiazanie, zbior_rozw=zbior_rozw, rows=rows)
    if -1 == zmienna1:
        pass
    else:
        najlepsza_suma = zmienna1
    zmienna2 = little(macierz[:], najlepsza_suma, suma, rozwiazanie, zbior_rozw=zbior_rozw, rows=rows, zabraniam=True)
    if -1 == zmienna2:
        pass
    else:
        najlepsza_suma = zmienna2
    # zwracamy najlepsza sume
    return najlepsza_suma


def main():
    suma = 0
    najlepsza_suma = inf
    rozwiazanie = []
    # Macierz z wykładu
    #macierz = np.array([[inf, 5, 4, 6, 6],
    #                    [8, inf, 5, 3, 4],
    #                    [4, 3, inf, 3, 1],
    #                    [8, 2, 5, inf, 6],
    #                    [2, 2, 7, 0, inf]])
    #rows = macierz.shape[0]
    #print(macierz)
    #suma = little(macierz, najlepsza_suma, suma, rozwiazanie, rows=rows)
    x = np.random.randint(low=0, high=10, size=(6, 6))
    rowsx = x.shape[0]
    x = x.astype('float')
    for i in range(rowsx):
        x[i][i] = inf
    print(x)
    suma = little(x, najlepsza_suma, suma, rozwiazanie, rows=rowsx)
    print(suma)
    print(rozwiazanie)


main()