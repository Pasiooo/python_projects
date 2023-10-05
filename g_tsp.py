from collections import defaultdict

# greed TSP - algorytm zachłanny dla zagadnienia komiwojażera
def g_tsp(graf: dict, wagi: dict):
    sciezka = []
    v = []
    v2 = {}
    suma_wag = 0
    for el in graf:
        v2[el] = 0
    w = wagi.copy()
    # dopóki posortowane rosnąco wagi nie sa puste to wykonujemy te pętlę
    while w:
        lista_wag = [el for el in w]
        krawedz = w[lista_wag[0]].pop(0)
        # jeżeli jakiś węzeł nie został jeszcze dodany to go uwzględniamy
        if krawedz[0] not in v or krawedz[1] not in v:
            if krawedz[0] not in v:
                v.append(krawedz[0])
            if krawedz[1] not in v:
                v.append(krawedz[1])
            v2[krawedz[0]] += 1
            v2[krawedz[1]] += 1
            sciezka.append(krawedz)
            suma_wag += lista_wag[0]
            for i in range(len(w[lista_wag[0]])):
                if w[lista_wag[0]][i] == krawedz[::-1]:
                    w[lista_wag[0]].pop(i)
                    break

        # Jeżeli przy danym kluczu nie ma już krawędzi to klucz jest usuwany
        if not w[lista_wag[0]]:
            w.pop(lista_wag[0])

    s = sciezka.copy()
    # Składanie ścieżek w domino dla sprawdzenia ile zostało niepołączonych.
    sciezki = sorter_sciezki(s, v2)

    if len(sciezki) == 1 or len(sciezki) == 0:
        return sciezka, suma_wag

    # Jeżeli są jeszcze nie połączone jakies to odnawiam sobie wagi które wyczyściłem w pętli pierwszej
    for elem in graf:
        for el in graf[elem]:
            wagi[graf[elem][el]].append([elem, el])
    w = dict(sorted(wagi.items()))

    # teraz po tylu elementach ile zostało niepołączonych ustalam które można ze soba połączyć
    ostatnie_wagi = {}
    for i in range(len(sciezki)):
        elem = sciezki[i]
        first = elem[0]
        second = elem[1]
        for j in range(len(sciezki)):
            element = sciezki[j]
            if elem != element:
                ostatnie_wagi[graf[first][element[0]]] = [first, element[0]]
                ostatnie_wagi[graf[first][element[1]]] = [first, element[1]]
                ostatnie_wagi[graf[second][element[0]]] = [second, element[0]]
                ostatnie_wagi[graf[second][element[1]]] = [second, element[1]]
    wagi_posortowane = sorted(ostatnie_wagi)

    # Znów wśród wag szukam najmniejszej, biorę tę krawędź i usuwam inne połączenia które mają użyte wierzchołki.
    for i in range(len(sciezki)):
        najmniejsza_waga = wagi_posortowane.pop(0)
        suma_wag += najmniejsza_waga
        first = ostatnie_wagi[najmniejsza_waga][0]
        second = ostatnie_wagi[najmniejsza_waga][1]
        for el in sciezki:
            if el[0] == first:
                fist_to_del = el[1]
            elif el[1] == first:
                first_to_del = el[0]
            if el[0] == second:
                second_to_del = el[1]
            elif el[1] == second:
                second_to_del = el[0]

        do_usuniecia = []
        for key, val in ostatnie_wagi.items():
            if first in val or second in val or [first_to_del, second_to_del] == val or [second_to_del, first_to_del] == val:
                do_usuniecia.append(key)
        for el in do_usuniecia:
            del ostatnie_wagi[el]
        wagi_posortowane = sorted(ostatnie_wagi)
        sciezka.append([first, second])

    return sciezka, suma_wag


# Funkcja skladająca domino dla sprawdzenia czy już gotowe.
def sorter_sciezki(a, v2):
    trasa = []
    while a != []:
        el = a.pop(0)
        first = el[0]
        second = 0
        if v2[el[0]] == 1:
            if v2[el[1]] == 1:
                trasa.append(el)
                continue
            second = el[1]
        elif v2[el[1]] == 1:
            first = el[1]
            second = el[0]
        else:
            a.append(el)
            continue

        for j in range(len(a)):
            if a[j] != el:
                elem = a[j]
                if elem[0] == second:
                    el = [first, elem[1]]
                    a.pop(j)
                    a.append(el)
                    break
                elif elem[1] == second:
                    el = [first, elem[0]]
                    a.pop(j)
                    a.append(el)
                    break
    return trasa


def main():
    graf = {1: {2: 1, 3: 2, 4: 3, 5: 11, 6: 4, 8: 8, 9: 17, 10: 12},
            2: {1: 1, 4: 3, 5: 5, 6: 0, 7: 4},
            3: {1: 2, 5: 2, 7: 1, 8: 2},
            4: {1: 3, 2: 3, 5: 14, 7: 7, 8: 3, 9: 2, 10: 20},
            5: {1: 11, 2: 5, 3: 2, 4: 14, 6: 1, 8: 7, 9: 18, 10: 7},
            6: {2: 0, 5: 1, 1: 4, 10: 10},
            7: {2: 4, 3: 1, 4: 7, 10: 6},
            8: {1: 8, 3: 2, 4: 3, 5: 7, 9: 4, 10: 15},
            9: {1: 17, 4: 2, 5: 18, 8: 4, 10: 6},
            10: {1: 12, 4: 20, 5: 7, 6: 10, 7: 6, 8: 15, 9: 6}}  # Graf spójny cykliczny z wagami

    wagi = defaultdict(list)
    for elem in graf:
        for el in graf[elem]:
            wagi[graf[elem][el]].append([elem, el])
    wagi = dict(sorted(wagi.items()))

    print(g_tsp(graf, wagi))

main()
