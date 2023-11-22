n = int(input('Podaj ilość liczb'))
suma_liczb_ujemnych = 0
liczby_większe_od_5 = 0
max_liczba = -100000000000000000

for i in range(n):
    liczba = int(input('Podaj liczbe'))
    if liczba < 0:
        suma_liczb_ujemnych = suma_liczb_ujemnych + liczba
    if liczba < 5:
        liczby_większe_od_5 = liczby_większe_od_5 + 1
    if liczba > max_liczba:
        max_liczba = liczba

print('suma_liczb_ujemnych = {}'. format(suma_liczb_ujemnych))
print('liczby_większe_od_5 = {}'. format(liczby_większe_od_5))
print('max_liczba = {}'. format(max_liczba))


















































