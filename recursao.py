"""
Exercício em Python
Digite um número e saiba seu valor em fatorial

Equação de fatorial

n! = n*(n-1) * n(n-2)*...*1
f(n) = n*(n-1), se n>1
"""
print('--------------------------------')

f = int(input('Digite um número: '))
def fatorial(numero):
    if numero == 1:
        return 1
    return numero * fatorial(numero -1)

def fatorial_for(f):
    resultado = 1

    for i in range(1, f + 1):
        resultado = resultado * i
    return resultado

print(f'O fatorial de {f} é: {fatorial_for(f)}')