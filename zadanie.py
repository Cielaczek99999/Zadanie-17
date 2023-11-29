import random

#Losowanie liczby z zakresu od <-100, 100>
#Liczba = int(random.random() * (koniec - początek))) + początek
liczba = int(random.random() * 200) - 100
print(liczba)

lista=[]

for i in range(20):
    #Liczba = int(random.random() * 200) - 100
    #lista.append(liczba)
    lista.append(int(random.random() * 200) - 100)
print(lista)