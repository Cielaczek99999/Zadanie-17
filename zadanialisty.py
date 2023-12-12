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

#Funkcje:

text_lista.remove('')

print('$'.join(text_lista))

#Zadanie 4

filenames = ['view.jpg', 'bear.jpg', 'ball.png']
filenames.insert(0, 'phone.jpg')

#Zadanie 5

day1 = ['3984', '9042', '4829', '2380']
day2 = ['4231', '5234', '1345', '2455']
day1.extend(day2)
print(day1)

#Zadanie 6

techs = ['python', 'java', 'sql', 'aws']
tech.sort(reverse=True)
print(techs)

#Zadanie 7

hashtags = ['summer', 'time', 'vibes']
wynik = '#'.join(hashtags)
print(wynik)
#wynik = '#' + '#'.join(hashtags)

#Zadanie 8

scorers = [27, 8, 15, 2, 9, 10, 21, 4, 20, 5]
scorers.sort(reverse=True)
print('3 najlepsze wyniki:{}'.format(scorers[0.:3]))

#wynik = list(map(str, scorers[:3]))
#print('\n'.join(wynik))
#Przerobienie intgów na string

#Zadanie 9
players = ['LeBron', 'Kobe', 'Jordan']
scorers = [27, 18, 15]
players.pop(1)
popped_scores = scores.pop(1)
print(players)
print(scorers)
print(popped_scores)

#Zadanie 11

players = ['LeBron', 'Kobe', 'Jordan']
scorers = [27, 18, 15]
new_players = ['LeBron', 'Kobe']
new_scores = [27, 18]
players.extend(new_players)
scores.extend(new_scores)
print(players)
print(scorers)

#Zadanie 12

score_stack = []
score_stack.append('0-0')
print(score_stack[-1])
score_stack.append('1-0')
print(score_stack[-1])
score_stack.append('1-1')
print(score_stack[-1])
score_stack.append('1-2')
print(score_stack[-1])
wynik = score_stack.pop(-1)
print(wynik)
print('Sędzia popełnił błąd wynik to: {}'.format(score_stack[-1]))

#Zadanie 13
order_queue = []
order_queue.append(('Pen'))
order_queue.append(('Book', 'Mouse'))
order_queue.append(('Notebook', 'Pencil'))

print(order_queue[0])
order_queue.pop(0)

menu = [
    [
        'Spaghetti Bolognese',
        12.99,
        [
            'spaghetti',
            'tomato sauce',
            'ground beef',
            'onion',
        ],
    ],
    [
        'Caesar Salad',
        8.99,
        [
            'romaine lettuce',
            'croutons',
            'parmesan cheese',
            'Caesar dressing',
        ],
    ],
    [
        'Margherita Pizza',
        14.99,
        [
            'pizza dough',
            'tomato sauce',
            'mozzarella cheese',
            'basil',
        ],
    ],
    [
        'Cheeseburger',
        10.99,
        [
            'beef patty',
            'cheddar cheese',
            'lettuce',
            'tomato',
            'bun',
        ],
    ],
]
print(menu[2][2])