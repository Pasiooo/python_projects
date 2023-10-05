import math
import numpy as np


# programowanie dynamiczne - wyznaczanie optymalnej partii produkcyjnej
def tworzenie_tabeli(Ymin, Ymax, y6, q, n, g_xi, h):
    # Pomocniecze zmienne
    tab = np.zeros((Ymax - Ymin + 1, 2*n + 1))
    counter = 0
    ostatni_miesiac = True
    # Utworzenie pierwszej kolumny ze stanem magazynu
    for el in range(Ymin, Ymax+1):
        tab[counter][0] = el
        counter += 1
    # Przejscie po kolejnych etapach
    for etap in range(1, n+1):
        # Algorytm dla ostaniego miesiąca (pierwszego etapu)
        if ostatni_miesiac:
            ostatni_miesiac = False
            # idąc po stanach
            for stan in range(Ymax-Ymin+1):
                # sprawdzam ile dokupić
                ile_trzeba_dokupic = int(y6 - tab[stan][0] + q[etap-1])
                # aktualizuje tabele
                if ile_trzeba_dokupic < 0:
                    tab[stan][2*etap-1] = None
                    tab[stan][2*etap] = math.inf
                else:
                    tab[stan][2*etap-1] = ile_trzeba_dokupic
                    tab[stan][2*etap] = g_xi[ile_trzeba_dokupic]
        # Algorytm dla wszystkich pozostałych etapów po pierwszym
        else:
            for stan in range(Ymax - Ymin + 1):
                # Sprawdzam ile muszę dokupić minimalnie
                stan_magazynu = int(tab[stan][0])
                min_musimy_dokupic = q[etap-1] - stan_magazynu + Ymin
                min_cena = math.inf
                # Od minimalnej ilości elementów które muszę dokupić do maksymalnej
                for i in range(min_musimy_dokupic, len(g_xi)):
                    # Sprawdzam czy mogę dokupić tyle oraz czy cena bęzie mniejsza w tym przypadku
                    if Ymax - Ymin > i - q[etap-1] + stan_magazynu and min_cena > g_xi[i] + h[i - q[etap-1] + stan_magazynu] + tab[i - q[etap-1] + stan_magazynu][2*(etap-1)]:
                        min_cena = g_xi[i] + h[i - q[etap-1] + stan_magazynu] + tab[i - q[etap-1] + stan_magazynu][2*(etap-1)]
                        ile_trzeba_dokupic = i
                    # Aktualizuje tabele najmniejszą ceną i ilością rzeczy do dokupienia
                    tab[stan][2 * etap - 1] = ile_trzeba_dokupic
                    tab[stan][2 * etap] = min_cena
    return tab


def szukanie_najlepszej_konfiguracji(tab, y0, n, q, Ymin):
    konfiguracja = []
    # idąc od tyłu tabeli czyli po kolei misiącami
    while n:
        # Dodaje do konfiguracji ten miesiąc dla którego odpowiada stan magazynu
        konfiguracja.append(int(tab[y0 - Ymin][2*n-1]))
        # aktualizuje stan magazynu na kolejny miesiąc
        y0 = int(y0 + tab[y0 - Ymin][2*n-1] - q[n-1])
        n -= 1
    return konfiguracja


def main():
    Ymin = 2  # min pojemnosc magazynu
    Ymax = 6  # max pojemnosc magazynu
    y0 = 3  # stan magazynu na poczatek
    y10 = 3  # stan magazynu na koniec
    q = [1, 4, 3, 2, 0, 1, 3, 2]  # ilosc sztuk na miesiac do oddania
    n = 8  # dlugosc procesu w miesiacach
    g_xi = [0, 15, 18, 21, 24, 26, 27]  # cena dokupienia do 3 rzeczy
    h = [0, 1, 1, 2, 5, 6, 7]  # cena za przechowywanie w magazynie
    tab = tworzenie_tabeli(Ymin, Ymax, y10, q, n, g_xi, h)
    print(tab)
    najlepsza_konfiguracja = szukanie_najlepszej_konfiguracji(tab, y0, n, q, Ymin)
    print(najlepsza_konfiguracja)


main()
