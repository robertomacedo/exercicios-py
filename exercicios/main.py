"""
Calculadora simples em python
O objetivo é desenvolver a lógica não há uma preocupação com escrever menos código nesse momento.
"""
print('---------------------------------------')
print('CALCULADORA SIMPLES COM PYTHON')
print('---------------------------------------')

operacao = input('Digite a operação: (soma, mult, sub, div)')
numero1 = input('Digite o primeiro número: ')
numero2 = input('Digite o segundo númeor: ')

if operacao == 'soma':
    print(int(numero1) + int(numero2))
if operacao == 'mult':
    print(int(numero1) * int(numero2))
if operacao == 'sub':
    print(int(numero1) - int(numero2))
if operacao == 'div':
    print(int(numero1) / int(numero2))

else:
    print('Operação não foi possível.')

