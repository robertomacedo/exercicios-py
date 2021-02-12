def _torre_de_hanoi_recursivo(numero_de_disco, origem, destino, auxiliar):
    if numero_de_disco == 1:
        print(f'{origem} -> {destino} : {numero_de_disco}')
        return
    _torre_de_hanoi_recursivo(numero_de_disco - 1, origem, auxiliar, destino)
    print(f'{origem} -> {destino} : {numero_de_disco}')
    _torre_de_hanoi_recursivo(numero_de_disco - 1, auxiliar, destino, origem)


def torre_de_hanoi(numero_de_disco: int):
    _torre_de_hanoi_recursivo(numero_de_disco, origem='A', destino='B', auxiliar='C')


if __name__ == '__main__':
    for i in range(1, 7):
        print(f'#### Hanoi para {i} discos')
        torre_de_hanoi(i)

