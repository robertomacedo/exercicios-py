#Criar algoritimo para calcular e imprir números primos.
"""
Exercício em python, cálculo de números primos em uma lista
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


