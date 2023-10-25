
Gracze_druzyny1=int(input('Podaj liczbę graczy druzyny 1.'))
Gracze_druzyny2=int(input('Podaj liczbę graczy druzyny drugiej'))
if Gracze_druzyny1 == Gracze_druzyny2 ==2:
    print('Mecz mozna zaczac')
elif Gracze_druzyny1>2 and Gracze_druzyny2>2:
    print('Za duzo graczy, mecz się nie odbędzie.')
else:
    print('Zła liczba graczy')

lista =[1, 1, 1, 1,]
akcja = 1
druzyna1 =0
druzyna2=0
for i in lista:
    print('Akcja nr {}.'.format(akcja))
    D =int(input('Która druzyna wygrała akcje.'))
    if D==1:
      druzyna1= druzyna1 +1
    elif D==2:
        druzyna2 = druzyna2+1
    akcja = akcja+1
    lista.append(1)




'''for e in lista
    print(e)
    lista.append(1)'''
'''lista = [1, 1, 1, 1]
licznik = 0
#nieskończony for
for i in lista:
    #print(i)
    licznik = licznik + 1
    lista.append(1)
    if licznik >= 10:
        break'''


'''druzyna1 = int(input('Podaj liczbe punktów zdobytych przez druzyne 1.'))
druzyna2 = int(input('Podaj liczbe punktów druzyny drugiej'))
if druzyna1 > druzyna2:
    print('Druzyna 1 wygrała seta.')
elif druzyna1 < druzyna2:
    print('Druzyna 2 wygrała seta')
else:
    print('Druzyny zremisowały')'''
