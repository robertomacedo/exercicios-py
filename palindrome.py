"""
Lógica para impressão de palindromes de números inteiros
Início em zero até o valor que queira imprimir os palindromos.
Exemplo 0 100 o resultado é : 0 1 2 3 4 5 6 7 8 9 11 22 33 44 55 66 77 88 99

"""
x, y = map(int, input().split())
a = 0
for i in range(x, y+1):
    a = str(i)
    if (a == a[:: -1]):
        print(i, end=" ")
if(a == 0):
    print('Invalid')
