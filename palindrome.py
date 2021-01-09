"""
Lógica para impressão de palindromes de números inteiros
Início em zero até o valor que queira imprimir os palindromos.
Exemplo 0 100 o resultado é : 0 1 2 3 4 5 6 7 8 9 11 22 33 44 55 66 77 88 99

palindromo ocorre quando o sentido inverso seja de um texto ou número é o mesmo
exemplo 33 se escrito ao contrário continua 33, "ANA" escrito ao contrŕio continua "ANA" e é isso.
"""
print('Digite o primeiro número dê um espaço digite o segundo número,')
print('e será impresso os palindromos no intervalo dado.')

x, y = map(int, input().split())
a = 0
for i in range(x, y+1):
    a = str(i)
    if (a == a[:: -1]):
        print(i, end=" ")
if(a == 0):
    print('Invalid')
