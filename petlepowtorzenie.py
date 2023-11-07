'''for i in range(-10, 21): #od -10 do 21 - 1 =20
    print(i)'''


'''for i in range(-60, 101, 2): #od -60 do 100 co drugą
    print(i)

lista = [1]
j = -60
for i in lista:
    print(j)
    if j >= 100:
        break
    j = j + 2
    lista.append(1)''' #append powoduje nieskoczona petle
#Statystyki liczb na liście
lista2 = [-3, 0, -2, 1, 7, 5]#chodzenie po liscie
max_liczba = lista2[0]
suma = 0
licznik = 0
for i in lista2:
    suma = suma + i
    if i > max_liczba:
        max_liczba = i
    if i < 2 :
        licznik = licznik + 1
print('suma wynosi {}'. format(suma))
print('max liczba wynosi {}'. format(max_liczba))
print('liczba liczb mniejszych od 2 to {}'.format(licznik))