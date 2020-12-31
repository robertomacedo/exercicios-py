"""
Exercício em python
programa para gerar senhas
digite a quantidade de caracter e uma senha será gerada

"""
import string
from random import random, choice

print('-----------------------------------')
print('GERE UMA SENHA ALEATÓRIA')
print('')

size = int(input('Digite a quantidade de caracter: '))

values = string.ascii_letters
values += string.digits
values += string.punctuation
senha = ""

for i in range(size):
    senha += choice(values)
print('')
print(f'Sua senha de {size} caracter é:', senha)


