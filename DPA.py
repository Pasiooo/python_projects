import math

# Dijksta-Prima Algorytm - minimalne drzewo rozpinające grafu.
def DPA(G: dict, s: int) -> tuple((list[tuple], int)):
    suma: int = 0
    A: list = []  # lista krawędzi
    alfa: dict = {}  # lista przejść
    beta: dict = {}  # lista wag przejść
    # Zbiór weirzchołków G jeszcze nie odwiedzonych
    Q: list = [el for el in G]
    # usuwamy startowy
    Q.remove(s)
    u_aktualne = s
    # nadanie wag początkowych
    for el in Q:
        alfa[el] = 0
        beta[el] = math.inf
    # dopóki Q nie jest puste
    while Q:
        # dla sąsiadów u_aktualnego
        for u in G[u_aktualne]:
            # jeżeli sąsiad nie był jeszcze odwiedzony
            if u in Q:
                # jeżeli waga mniejsza to podmieniamy
                if beta[u] > G[u_aktualne][u]:
                    alfa[u] = u_aktualne
                    beta[u] = G[u_aktualne][u]
        min_waga = math.inf
        # szukanie u = arg min(beta[u])
        for u in Q:
            if beta[u] < min_waga:
                min_waga = beta[u]
                u_kolejne = u
        # dodanie przejścia do listy
        A.append((alfa[u_kolejne], u_kolejne))
        # czyszczenie odwiedzonych węzłów
        Q.remove(u_kolejne)
        del alfa[u_kolejne]
        del beta[u_kolejne]
        suma += min_waga
        # podmiana nowego sprawdzanego węzła
        u_aktualne = u_kolejne

    return A, suma


def main():
    G1 = {1: {2: 1, 3: 2, 4: 3, 6: 4},
          2: {1: 1, 4: 3, 5: 5, 6: 0, 7: 4},
          3: {1: 2, 5: 2, 7: 1, 8: 2},
          4: {1: 3, 2: 3, 7: 7, 8: 3, 9: 2},
          5: {2: 5, 3: 2, 6: 1, 8: 7},
          6: {2: 0, 5: 1, 1: 4, 10: 10},
          7: {2: 4, 3: 1, 4: 7, 10: 6},
          8: {3: 2, 4: 3, 5: 7, 9: 4},
          9: {4: 2, 8: 4, 10: 6},
          10: {6: 10, 7: 6, 9: 6}}  # Graf spójny cykliczny z wagami

    s: int = 1  # Start

    # wywołanie algorytmu dla grafu G2 i elementu 1
    lista_krawedzi, suma = DPA(G1, s)

    # rozwiązanie
    print(lista_krawedzi, suma)


main()
