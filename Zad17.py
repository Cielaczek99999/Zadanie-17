n = int(input('Podaj ile będzie liczb'))

suma=0
max_liczba = -1000000000
min_liczba= 1000000000
ile_mniejszych_od_3= 0
ile_w_przedziale = 0
for i in range(n):
    liczba = int(input('Podaj kolejną liczbę'))
    print('Podałeś liczbę' + str(liczba))
    #print(;Podałeś liczbę {}'.format(liczba)
    suma = suma + liczba
    #print(suma)
    if liczba > max_liczba:
        max_liczba = liczba

    if liczba < min_liczba:
        min_liczba= liczba
    if liczba < 3:
        ile_mniejszych_od_3 = ile_mniejszych_od_3 + 1
    if liczba > -2 and liczba <=11:
        ile_w_przedziale = ile_w_przedziale +1

print('suma = {}'.format(suma))
print('średnia ={}'. format(suma / n))
print('max={}'. format(max_liczba))
print('mniejszych od 3 było = {} liczb'.format(ile_mniejszych_od_3))
print('w przedziale było = {} liczb'. format(ile_w_przedziale))
