
import string
from random import random, choice


values = string.ascii_letters
values += string.digits
values += string.punctuation
tamanho = 9
senha = ""

#print(values)

for i in range(tamanho):
    senha += choice(values)

print(senha)


