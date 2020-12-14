"""
Embaralhamento de lista e organização da lista
usando lib randon e shuffle
bem como a lib sort
"""
import random


lista_p = []

lista_p = ['Antonio']
lista_p.append('Roberto')
lista_p.append('Emily')
lista_p.append('Macleusa')

lista_p.sort()

random.shuffle(lista_p)

for nome in lista_p:
    print(nome)