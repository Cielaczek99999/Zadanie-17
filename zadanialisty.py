cities = ['Warszawa', 'Łódź', 'Gdańsk']
cities.append('Gdańsk')

idx = ['001', '002', '001', '003', '001']
print.(idx.count('001'))

text = 'Programowanie w języku Python'
text1 = text.lower() #zmiana wszystkich liter na małe
text2 = text.upper() #zamiana liter na duże

text = text.lower()
print(text)

#Zamiana na polski
#1
text_lista = list(text1)
for i in range(len(text_lista)):
    if text_lista[1] == 'ę'
        text_lista[i] = 'e'
print(text_lista)

#Usuwanie duplikatów

lista_pomocnicza = []

for i in range(len(text_lista)):
    if lista_pomocnicza.count(text-lista[i]) == 0:
        lista_pomocnicz.append(text_lista[i])
print(lista_pomocnicza)

#sposób 2 - z użyciem setów
#set(text_lista)) - zamieniamy listę na zbiór (usuwamy duplikaty)
#list(set(text_lista)) - zamieniamy z powrotem zbiór na listę
text_lista = list(set(text_lista))
print(text_lista)

#Sposób 3 - z listą dodatkową i operator in
lista_pomocnicza = []

for i in range(len(text_lista)):
    if not(text_lista[i] in lista_pomocnicza): #sprawdzamy, czy literka nie jest na liście
        lista_pomocnicza.append(text_lista[i])
print(lista_pomocnicza)