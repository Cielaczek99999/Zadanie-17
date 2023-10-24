n = int(input('Podaj ile będzie liczb'))
lista = []
for i in range(n):
    liczba = int(input('Podaj kolejną liczbę: '))
    lista.append(liczba)

#print(liczba)
print('suma = {}'.format(sum(lista)))
print('średnia = {}'.format(sum(lista) / n))
print('max = {}'. format(max(lista)))
print('min = {}'. format(min(lista)))