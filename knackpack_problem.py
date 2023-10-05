import numpy as np


def decyzja(z, w, ogr, ilosc):
    # Pomocnicza tablica zer
    tab = np.zeros((ogr + 1, ilosc + 1))

    # Jedziemy po wszystkich kolumnach i wierszach
    for col in range(1, ilosc + 1):
        for row in range(1, ogr + 1):
            # Jeżeli przedmiot mieści się do plecaka to go sprawdzamy
            if w[col-1] <= row:
                # Patrzymy czy wzięcie go zwiększy nam zysk
                tab[row][col] = max(z[col-1] + tab[row-w[col-1]][col-1], tab[row][col-1])
            # Jak się nie mieści to zysk przepisujemy a poprzedniej kolumny
            else:
                tab[row][col] = tab[row][col-1]
    # Zwracam tablicę i maksymalny zysk
    return tab, tab[ogr][ilosc]


def main():
    # Deklaracja zmiennych
    zyski = np.array([4, 1, 3, 4, 2, 5, 3, 2, 6, 1])
    wagi = np.array([6, 2, 3, 6, 1, 3, 4, 8, 10, 1])
    ilosc_przedmoitow = len(wagi)
    ograniczenie_wag = 20

    # Wywołanie funkcji do obliczenia zysku
    tab, max_zysk = decyzja(zyski, wagi, ograniczenie_wag, ilosc_przedmoitow)
    # Printuje tablice
    print(tab)

    # Deklaracja zmiennych do szukania najlepszej ścieżki
    indeksy = []
    aktualny_rzad = ograniczenie_wag
    aktualna_kolumna = ilosc_przedmoitow
    aktualny_zysk = tab[aktualny_rzad][aktualna_kolumna]
    # Dopóki zysk jest różny od 0
    while aktualny_zysk:
        # Jeżeli dodanie przedmiotu zmienia nam zysk to go uwzględniamy
        if aktualny_zysk != tab[aktualny_rzad][aktualna_kolumna - 1]:
            indeksy.append(1)
            aktualny_rzad -= wagi[-len(indeksy)]
            aktualna_kolumna -= 1
            aktualny_zysk = tab[aktualny_rzad][aktualna_kolumna]
        # Jeżeli nie to przechodzimy dalej
        else:
            indeksy.append(0)
            aktualna_kolumna -= 1

    print("Kolejne elementy które bierzemy w najoptymalniejszym zapakowaniu to:")
    print(indeksy[::-1])
    print("Maksymalny zysk to:", max_zysk)


if __name__ == "__main__":
    main()
