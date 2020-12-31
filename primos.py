#Criar algoritimo para calcular e imprir números primos.
"""
Exercício com números primos em Python.
Digite um valor o programa mostrará
quantas vezes esse número foi dividido
e indicará se é ou não primo pelo número
de divisões, ou seja, duas vezes é primo,
mais de duas não é primo.
"""

num = int(input('Digite um número: '))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[34m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print('{}'.format(c), end='')
print('\n\033[mO número {} foi dividido {} vezes'. format(num, total))
if total == 2:
    print('E por isso é primo.')
else:
    print('E por isso Não é primo.')


