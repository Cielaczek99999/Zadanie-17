lista = [1]
a = 1
punkty1 = 0
punkty2 = 0
for x in lista:
    print('Akcja nr {}'. format(a))
    druzyna = int(input('Podaj która druzyna wygrała akcję.'))
    if druzyna ==1:
        punkty1 = punkty1 +1
    else:
        punkty2 = punkty2 + 1
    print('{} : {}'.format(punkty1, punkty2))
    if punkty1 >=5 or punkty2 >= 5:
        roznica = abs(punkty1 - punkty2)
        if roznica >= 2:
            if punkty1
                print('Koniec wygrała druzyna 1')
            else:
                print('Koniec wygrała druzyna 2')
            break
    a = a + 1
    lista.append(1)