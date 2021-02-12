chamadas_hanoi = 0

"""
Estudando o clássico problema da torre de hanoi, o algorítmo vai apresentar a quantidade de chamadas
da funão dependendo da quantidade dediscos na torre.

o resultado das chamadas nos mostra que a função para esse problema eh exponencial

f(n-1)

"""

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
    for i in range(1, 7):
        print(f'#### Hanoi para {i} discos')
        torre_de_hanoi(i)
        print(f'***********{chamadas_hanoi} chamadas')

