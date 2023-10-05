# Depth-first search
def DFS(G: dict[int], s: int) -> dict[int]:
    licznik = 0
    # słownik do przedstawienia elementów w nowej kolejności
    numeracja_elementow = {}
    # Liczby naturalne 1,...,n
    lista_numerow = [el for el in range(1, len(G) + 1)]
    lista = [s]  # pomocnicza lista, z pierwszym elementem
    while lista:  # dopoki lista nie jest pusta
        v = lista.pop()  # bierzemy element z listy
        # sprawdzamy czy ten element byl juz sprawdzany
        if v not in numeracja_elementow:
            # dodajemy mu numer
            numeracja_elementow[v] = lista_numerow.pop(0)
            # bierzemy jego sąsiadów
            lista_zapasowa = G[v][::-1]
            # zapisujemy sąsiadów do listy elementów do sprawdzenia
            for u in lista_zapasowa:
                licznik += 1
                lista.append(u)
    # Sprawdzanie cykliczności grafu z ilości ruchów ile wykonał
    if licznik == (len(numeracja_elementow) - 1)*2:
        print('Graf acykliczny')
    else:
        print('Graf cykliczny')
    return numeracja_elementow  # zwracamy wynik

def main():
    G1 = {1: [2, 3, 4],
         2: [1, 5, 6],
         3: [1, 7],
         4: [1, 8, 9],
         5: [2],
         6: [2],
         7: [3, 10],
         8: [4],
         9: [4],
         10: [7]}  # Graf spójny acykliczny

    G2 = {1: [2, 3, 4, 6],
          2: [1, 5, 6, 7],
          3: [1, 7, 8],
          4: [1, 7, 8, 9],
          5: [2, 6],
          6: [2, 5, 1, 10],
          7: [2, 3, 4, 10],
          8: [3, 4, 9],
          9: [4, 8],
          10: [6, 7]}  # Graf spójny cykliczny

    G3 = {1: [2, 3, 6],
          2: [1, 5, 6, 7],
          3: [1, 7],
          4: [8, 9],
          5: [2, 6],
          6: [2, 5, 1, 10],
          7: [2, 3, 10],
          8: [4, 9],
          9: [4, 8],
          10: [6, 7]}  # Graf niespójny cykliczny

    s: int = 1  # Start
    # wykonanie się algorytmu DFS
    numeracja_elementow = DFS(G3, s)

    # Wyświetlanie wyniku
    for value, key in numeracja_elementow.items():
        print("Element nr.", key, " ma indeks", value)

    # Sprawdzanie czy graf jest spójny
    if len(G3) != len(numeracja_elementow):
        print("Graf jest niespojny!")
    else:
        print('Graf jest spojny!')

main()
