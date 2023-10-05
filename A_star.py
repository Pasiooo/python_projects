import math

# Poszukiwanie najkrótszej ścieżki w grafie
def a_star(graf: dict, s: str, k: str, h: dict):
    Tz = [] # z nich już wyszedłem
    To = [] # do nich dopiero dotarłem
    f = {} # funkcja długości
    g = {} # odleglosc miedzy miastami
    u = s # miasto w ktorym aktualnie jestem
    h_aktualne = h.copy() # zapisanie odleglosci do nowej zmiennej
    # dodatkowa zmienna do sprawdzania nowych odleglosci
    for el in h:
        h[el] = math.inf
    # aktualnie przebyta dlugosc
    sciezka = 0
    # zapisane wszystkie sciezki, najlepsze
    najlepsza_sciezka = {}
    while True:
        # usuwamy miasto z ktorego wychodzimy
        if u in To:
            To.remove(u)
        # sprawdzamy sasiednie miasta
        for el in graf[u]:
            # miasta w ktorych jeszcze nie bylismy
            if el not in Tz:
                g[el] = graf[u][el]
                # sprawdzamy czy poprawia sie odleglosc
                if h[el] > g[el] + h_aktualne[el] + sciezka:
                    f[el] = g[el] + h_aktualne[el] + sciezka
                    h[el] = g[el] + h_aktualne[el] + sciezka
                    # aktualizujemy najlepsza sciezke
                    if u not in najlepsza_sciezka:
                        najlepsza_sciezka[u] = u
                    # tym prosze sie nie przejmowac to jest tylko dla ułatiwenia żeby wszystko było w jenej liście
                    if type(najlepsza_sciezka[u]) is list:
                        zmienna = najlepsza_sciezka[u].copy()
                        zmienna.append(el)
                    else:
                        zmienna = [najlepsza_sciezka[u], el]
                    najlepsza_sciezka[el] = zmienna
                # dodajemy do listy sąsiadów
                if el not in To:
                    To.append(el)
        # dodajemy do odwiedzonych miasto z ktorego wychodzimy
        Tz.append(u)
        # Jak było ono Krakowem to koniec
        if u == k:
            break
        odleglosc = math.inf
        # aktualizowanie odleglosci
        for el in To:
            if el not in Tz:
                if f[el] < odleglosc:
                    u = el
                    odleglosc = f[el]

        # obliczanie sciezki do u
        sciezka = 0
        for i in range(len(najlepsza_sciezka[u]) - 1):
            miejsce1 = najlepsza_sciezka[u][i]
            miejsce2 = najlepsza_sciezka[u][i + 1]
            sciezka += graf[miejsce1][miejsce2]

    # Ostateczne obliczenie drogi do przebycia z najkrotszej sciezki
    ostateczna_sciezka = najlepsza_sciezka['Krakow']
    ostateczna_odleglosc = 0
    miejsce1 = ''
    miejsce2 = ''
    for i in range(len(ostateczna_sciezka) - 1):
        miejsce1 = ostateczna_sciezka[i]
        miejsce2 = ostateczna_sciezka[i + 1]
        ostateczna_odleglosc += graf[miejsce1][miejsce2]

    return ostateczna_sciezka, ostateczna_odleglosc

def main():
    graf = {'Opole': {'Czestochowa': 97, 'Strzelce': 33, 'Gliwice': 82, 'Kedzierzyn': 54},
          'Czestochowa': {'Opole': 97, 'Strzelce': 77, 'Dabrowa': 63, 'Wolbrom': 85, 'Koniecpol': 45},
          'Koniecpol': {'Czestochowa': 45, 'Wolbrom': 53},
          'Strzelce': {'Opole': 33, 'Czestochowa': 77, 'Bytom': 51, 'Gliwice': 39},
          'Kedzierzyn': {'Opole': 54, 'Gliwice': 38},
          'Gliwice': {'Kedzierzyn': 38, 'Opole': 82, 'Strzelce': 39, 'Bytom': 21, 'Katowice': 29, 'Tychy': 33},
          'Bytom': {'Gliwice': 21, 'Strzelce': 51, 'Katowice': 13, 'Dabrowa': 28},
          'Dabrowa': {'Bytom': 28, 'Czestochowa': 63, 'Olkusz': 25, 'Katowice': 19},
          'Olkusz': {'Dabrowa': 25, 'Skala': 24, 'Krakow': 42},
          'Wolbrom': {'Czestochowa': 85, 'Koniecpol': 53, 'Miechow': 21, 'Skala': 19},
          'Miechow': {'Wolbrom': 21, 'Slomniki': 16},
          'Slomniki': {'Miechow': 16, 'Krakow': 24},
          'Katowice': {'Gliwice': 29, 'Bytom': 13, 'Dabrowa': 19, 'Krakow': 79, 'Chrzanow':34, 'Tychy': 19},
          'Skala': {'Olkusz': 24, 'Wolbrom': 19, 'Krakow': 22},
          'Tychy': {'Gliwice': 33, 'Katowice': 19, 'Oswiecim': 19},
          'Oswiecim': {'Tychy': 19, 'Chrzanow': 21, 'Krakow': 68},
          'Chrzanow': {'Oswiecim': 21, 'Katowice': 34, 'Krakow': 48},
          'Krakow': {}} # Graf spójny cykliczny z wagami

    h = {'Opole': 175, 'Czestochowa': 113, 'Koniecpol': 93, 'Strzelce': 144,
         'Kedzierzyn': 145, 'Gliwice': 107, 'Bytom': 86, 'Dabrowa': 63,
         'Olkusz': 41, 'Wolbrom': 42, 'Miechow': 35, 'Slomniki': 22,
         'Katowice': 70, 'Skala': 21, 'Tychy': 73, 'Oswiecim': 57,
         'Chrzanow': 46, 'Krakow': 0}
    # Start, koniec
    s, k = 'Czestochowa', 'Krakow'

    print(a_star(graf, s, k, h))


main()
