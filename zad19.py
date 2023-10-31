liczba_uczniow = int(input('Podaj liczbę uczniów.'))

for u in range(1, liczba_uczniow + 1):
    print('*****UCZEŃ NR {}*****'. format(u))
    l_ocen= int(input('Podaj liczbę ocen ucznia nr {}'))
    suma_licznik = 0
    suma_mianownik = 0
    for o in range(1, l_ocen + 1):
        ocena = int(input('Podaj ocenę nr {} ucznia nr {}'.format(o, u)))
        waga = int(input('Podaj wagę oceny nr {} ucznia nr {}'.format(o, u)))
        suma_licznik = suma_mianownik + waga * ocena
        suma_mianownik = suma_mianownik + waga
    srednia = suma_licznik / suma_mianownik
    ocena_koncoworoczna = 0
    if srednia >=1.91:
        ocena_koncoworoczna = 1
    elif srednia >=2.75:
        ocena_koncoworoczna = 2
    elif srednia >=3.75:
        ocena_koncoworoczna = 3
    elif srednia >= 4.51:
        ocena_koncoworoczna = 4
    elif srednia >= 5.21:
        ocena_koncoworoczna = 5
    else:
        ocena_koncoworoczna = 6
        print('{}\t{}\t{}'. format(u, srednia, ocena_koncoworoczna))