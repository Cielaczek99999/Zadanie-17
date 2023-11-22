#używamy gdy znamhy warunek trwania ale nie wiemy ile razy ma się wykonać
'''while True:
    print('OK')'''

'''for i in range(10):
print('coś')'''

#Używamy gdy wiemy ile będzie powtórzeń (lub ta informacja jest obliczana w tracie programu)
tajne_haslo = "gd23040"
haslo= ''
for i in lista:
    haslo=input('Podaj haslo')
    if haslo == tajne_haslo:
        break
    lista.append(1)

'''while haslo != tajne_haslo:
    haslo = input('Podaj hasło')'''

#pętla while przerobiona na for
i = 0
while True:
    if i >= 6:
        break
    print(i)
    i = i + 1



while haslo != tajne_haslo:
    if ile_prob >=3:
        print('Nie ma hasła = nie ma dostępu.')
        exit()
        ile_prob = ile_prob + 1
        haslo = input('Podaj haslo')
print('dostałeś się do systemu')
