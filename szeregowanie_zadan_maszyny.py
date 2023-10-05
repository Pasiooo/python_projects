import numpy as np
import random
import math


# Algorytm CDS dla 4 maszyn z użyciem algorytmu Johnsona - szeregowanie zadań
def two_m_kolejnosc(z):
    # Wielkość problemu plus pomocnicze zmienne.
    temp_z = z.copy()
    rows, cols = temp_z.shape
    s_row, s_col = 0, 0
    beg_id = 0
    end_id = cols - 1
    swap = 0
    swap_dict = {el: el for el in range(cols)}
    # sortowanie przez zmienianie
    while swap < cols:
        smallest = math.inf
        swap += 1
        # szukam najmniejszego elementu w całej macierzy.
        for row in range(rows):
            for col in range(beg_id, end_id + 1):
                if temp_z[row][col] < smallest:
                    smallest = temp_z[row][col]
                    s_row, s_col = row, col
        # Sprawdzam czy najmniejszy jest w pierwszym rzędzie czy w drugim
        # podmieniam miejsca i zappisuje nowa kolejnosc kolumn.
        if s_row == 0:
            temp_z[0][beg_id], temp_z[0][s_col] = temp_z[0][s_col], temp_z[0][beg_id]
            temp_z[1][beg_id], temp_z[1][s_col] = temp_z[1][s_col], temp_z[1][beg_id]
            swap_dict[beg_id], swap_dict[s_col] = swap_dict[s_col], swap_dict[beg_id]
            beg_id += 1
        else:
            temp_z[0][end_id], temp_z[0][s_col] = temp_z[0][s_col], temp_z[0][end_id]
            temp_z[1][end_id], temp_z[1][s_col] = temp_z[1][s_col], temp_z[1][end_id]
            swap_dict[end_id], swap_dict[s_col] = swap_dict[s_col], swap_dict[end_id]
            end_id -= 1
    # Zwracamy listę uporządkowanych kolumn
    return list(swap_dict.values())


def swap(z, swap_list):
    rows, cols = z.shape
    # zamiana kolumn listy.
    for row in range(rows):
        z[row][:] = z[row][swap_list]


def time(z):
    # Kopia listy z zadaniami i pomocnicze zmienne
    czas_zadan = z.copy()
    rows, cols = czas_zadan.shape
    prev_el = 0
    # Uzupełnienie pierwszego rzędu
    for col in range(cols):
        czas_zadan[0][col] += prev_el
        prev_el = czas_zadan[0][col]
    # Uzupełnienie pozostałych rzędów
    for row in range(1, rows):
        prev_el = czas_zadan[row - 1][0]
        for col in range(cols):
            czas_zadan[row][col] += prev_el
            if col < cols - 1:
                prev_el = max(czas_zadan[row][col], czas_zadan[row - 1][col + 1])
    return czas_zadan


def wywolanie_funkcji(z, zadania_random):
    print("zadania:\n", z)

    swap_list = two_m_kolejnosc(z)
    print('swap_list:\n', swap_list)

    temp_z = zadania_random.copy()
    swap(temp_z, swap_list)
    print("Posegregowane zadania:\n", temp_z)

    czas_zadan = time(temp_z)
    print("Czas zadan:\n", czas_zadan)

    return czas_zadan[-1][-1]


def main():
    # Generowanie losowych 10 zadań dla 4 maszyn.
    zadania_random = np.array([[random.randint(1, 20) for _ in range(10)],
                               [random.randint(1, 20) for _ in range(10)],
                               [random.randint(1, 20) for _ in range(10)],
                               [random.randint(1, 20) for _ in range(10)]])
    print("Wylosowane zadania:\n", zadania_random)
    # Pomocnicze zmienne
    min_czas = math.inf
    nr_wywolania = 0
    rows, cols = zadania_random.shape
    # Wszystkie przypadki M1, M2 oraz M3.
    for i in range(1, rows):
        print("\nZadanie pomocnicze r =", i)
        # Tworznie macierzy z dwoma rzędami o sumach poszczególnych rzędów
        z1 = np.zeros(cols)
        z2 = np.zeros(cols)
        for col in range(cols):
            for row in range(i):
                z1[col] += zadania_random[row][col]
                z2[col] += zadania_random[rows - row - 1][col]
        z = np.array([z1, z2])
        czas = wywolanie_funkcji(z, zadania_random)
        if czas < min_czas:
            min_czas = czas
            nr_wywolania = i
    print("\nMinimalny czas ukonczenia zadan to:", min_czas, "dla wywolania nr:", nr_wywolania)


main()