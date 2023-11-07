#Pętle zagnieżdżone
'''for i in range(1, 11):
    for j in range(1, 11):
        print('{} {}'. format(i, j))'''
#print bez przejscia do nowej linii
print('ok', end = ' ')
print('ko"')

for i in range(1, 11):
    print(i, end = ' ')

#tabliczka mnozenia
'''for i  in range(1, 11):
    for j in range(1, 11):
        print('{}'. format(i * j), end = '\t')
        print()'''
#Wzorki z gwiazdek
n = int(input('Podaj rozmiar trojkata'))
for i in range(n):
    for j in range(i + 1):
        print('*', end = '')
        #print('-'.join(lista))
    print()

#Metoda bez listy
n = int(input('Podaj rozmiar przekątnej'))
for i in range(n):
    for j in range(i):
        print(' ', end = ' ')
    print('*')