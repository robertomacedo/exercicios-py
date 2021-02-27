chamadas_hanoi = 0

"""
Algoritmo torre de hanoi

f(n-1)

"""

a = int(input('Número de discos: '))

def _torre_de_hanoi_recursivo(numero_de_disco, origem, destino, auxiliar):
    """
    f(n) = 1 + 2 * f(n-1)
    f(n) = 1 + 2 * (1 + 2 * f(n-2)) -> 1 + 2 + 2 + 4 * f(n-2)

    :param numero_de_disco:
    :param origem:
    :param destino:
    :param auxiliar:
    :return:
    """
    global chamadas_hanoi
    chamadas_hanoi += 1
    if numero_de_disco == 1:
        print(f'{origem} -> {destino} : {numero_de_disco}')
        return
    _torre_de_hanoi_recursivo(numero_de_disco - 1, origem, auxiliar, destino)
    print(f'{origem} -> {destino} : {numero_de_disco}')
    _torre_de_hanoi_recursivo(numero_de_disco - 1, auxiliar, destino, origem)


def torre_de_hanoi(numero_de_disco: int):
    global chamadas_hanoi
    chamadas_hanoi = 0
    _torre_de_hanoi_recursivo(numero_de_disco, origem='A', destino='B', auxiliar='C')


if __name__ == '__main__':
    for i in range(1, a):
        print(f'#### Hanoi para {i} discos')
        torre_de_hanoi(i)
        print(f'***********{chamadas_hanoi} chamadas')

opc = int(input('Deseja continuar? \n1. Sim\n2. Sair\n'))
if opc == 1:
    torre_de_hanoi()
else:
    print('Saindo..')
