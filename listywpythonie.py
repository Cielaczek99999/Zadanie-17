'''lista = []
print(type(lista))

#wypełnianie listy:
#1. wpisujemy elementy na sztywno
lista1 = [1, 5, 2, 9, 0]

#2. powielanie listy
lista2 = [1] * 1000
print(lista2)

lista3 = [1, 2, 3] * 10
print(lista3)
#3. Konkatenacja - sklejanie list
lista4 = [1, 2, 3] + [4, 5, 6]
print(lista4)

#4. Dołączanie pojedynczych elementów na końcu listy:
lista5 = []
lista5.append(3)
lista5.append(7)
print(lista5)

#5. Wstawianie elementu na określonej pozycji
lista6= [1, 2, 3, 4, 7]
lista6.insert(1, 90)
print(lista6)

#6. Rozszerzenie listy o elementy innej listy
lista7 = [4, 0, 1, 7, 9]
lista7.extend([7, 1, 5])
print(lista7)

#II rozmiar listy
lista8 = [5, 6, 7]
print(len(lista8))

#III Zliczanie ile razy na liście pojawia się dany element
lista9 = [7, 9, 9, 9, 7, 6, 4, ,4, 4, 4, 4, 0]
print(lista9.count(4)) #Zliczamy ile było czwórek na liście

#IV Zamiana napisu na listę
slowo1 = 'informatyka'
lista10 = list(slowo1)
print(lista10)
print(lista10.count('a'))

# Zamiana listy na napis
lista11 = [4, 9, 7, 1]
slowo2 = str(lista11)
print(slowo2)
print(len(slowo2))

#V Wycinanie fragmentu listy
#1. Wyciąganie pojedynczego elementu
lista12 = [6, 1, 3, 5, 2]
print(lista12[3]) #chcemy się dostać do czwartego elemntu listy (o indeksie 3)

#2. Wyciąganie fragmentu listy
lista13 = [6, 1, 3, 8, 9, 1, 2, 5]
print(lista13[1:4]) #Wycinamy fragment od indeksu 1 (drugi element) do indeksu 3(czwarty element)


#wycięcie przedziału <1, 6) co 2 liczby
print(lista13[1:6:2])#1 - od indeksu 1 do indeksu 5 (bo 6 - 1) co dwie liczby

lista14 = list(range(0, 1001))
print(lista[0:1001:3])

print(lista14[::3]) #od początku do końca co trzy

#Indeksy wsteczne od -1 w dół
lista15 = [6, 1, 5, 3, 2, 9, 1]

#ostatni element - sposób 1
print(lista15[len(lista15)-1])


#ciekawy sposób na odwracanie listy (od elementu 5 co 3)
print(lista15[-5:-3])


#Listy - przydatne funkcje
#1. Sortowanie

lista16.sort() #domyślne rosnąco
print(lista16)


lista16 = [4, -1, 7, 2, 4, -10, 8]
lista16.sort(reverse=True)
print(lista16)

#2. Odwracanie
slowo3 = 'abbcnno'
lista17 = list(slowo3)
lista17.reverse()
print(lista17)

#jak listę połączyć z powrotem w słowo
slowo3_po_odwr = ''.join(lista17)
print(slowo3_po_odwr)'''


#VI Usuwanie elementów z listy 
lista18 = ['kot', 2, 'pies', 7.4]

#usuwanie na podstawie nr elemntu
del lista18[2]
print(lista18)

#usuwanie na bazie wartości elementu
lista18.remove('kot')
print(lista18)

#VII Funkcj
#czyszczenie listy
#czyszczenie łopatologiczne
lista19 = [4, 9, 'kot', 'qwerty', 5, 99, 45]
lista19 = []

#czyszczenie eleganckie
lista20 = [4, 9, 'kot', 'qwerty', 5, 99, 45]
lista20.clear()
print(lista20)

#Sprawdzanie pod jakim indeksem jest dany element
Lista21 = ['matematyka', 'fizyka, informatyka', 'język polski', 'fizyka']
print(lista21.index('fizyka'))

#Chodzenie po liście z nadzorowaniem indeksów
Lista22 = ['jabłko', 'gruszka', 'winogrono', 'śliwka']

for nr, o in enumerate(lista22):
    print(nr, o)

#kopiowanie listy
#Sposób chałupniczy
lista_oryginalna = [3, 1, 7, 8, 11]
lista_kopia = lista_oryginalna
lista_kopia = lista_oryginalna

lista_kopia[2] = 67
print(lista_oryginalna)


#Jak można kopiować listy
#Sposób chałupniczy
Lista23 = [6, 1 , 2, 9, 1, 5]
Lista23_kopia = Lista23[::] #tzw, płytka kopia
lista23_kopia[2] = 78 #zmiana na kopii NIE POWODUJE zmian na oryginale
print(lista23)
print(lista23_kopia)

#elegancko
Lista24 = [6, 1 , 2, 9, 1, 5]
Lista24_kopia = Lista24.copy() #tzw, płytka kopia
lista24_kopia[2] = 78 #zmiana na kopii NIE POWODUJE zmian na oryginale
print(lista24)
print(lista24_kopia)

#VIII Wyrażenia listowe
lista_zwierzat = ['kapibara', 'kos', 'żyrafa', 'pies', 'orangutan', 'antylopa', 'tygrys', 'małpa']

#Chcemy, aby na liście pozostały tylko te nazwy zwierząt, które mają parzystą liczbę liter
#Przypomnienie - reszta z dzielenia
print(13 % 4) #obliczamy resztę z dzielenia liczby 13 przez 4

lista_zwierzat_parzyste = []

for z in lista_zwierzat:
if len(z) % 2 == 0: #Jeśli długość nazwy zwierzęcia daje przy dzieleniu przez 2 resztę 0 to...
    lista_zwierzat_parzyste.append(z)
print(lista_zwierzat_parzyste)

#Chcemy, aby na liście pozostały tylko te nazwy zwierząt, które maja parzystą liczbę liter - z wyrażeniami listy
lista_zwierzat_parzyste2 = [z for z in lista_zwierzat if len(z) % 2 ==0]
print(lista_zwierzat_parzyste2)

#Ile jest liczb podzielnych na 4 w zakresie podanym przez użytkownika
a = int(input('Podaj pierwszą liczbę'))
b = int(input('Podaj drugą liczbę'))
wynik = len([for i in range(a, b + 1) if i % 4 ==0])
lista_pod_4 = []
a = int(input('Podaj pierwszą liczbę'))
b = int(input('podaj drugą liczbę'))
for i in range(a, b + 1):
    if i = %4 == 0:
        lista_pod_4.append(i)
print(len(lista_pod_4))

