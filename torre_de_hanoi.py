contagem_de_chamdas_recusrivas = 0

def torre_de_hanoi_recursivo(numero_de_disco, origem, destino, auxiliar):
    global contagem_de_chmadas_recursivas
    contagem_de_chamadas_recursivas += 1
    if numero_de_disco == 1:
        print(f'{origem} -> {destino}: {numero_de_disco}')
        return
    _torre_de_hanoi_recursivo(numero_de_disco - 1, origem, auxiliar, destino)
    print(f'{origem} -> {destino}: {numero_de_disco}')
    _torre_de_hanoi_recursivo(numero_de_disco - 1, auxiliar, destino, origem)


def _torre_de_hanoi_recursivo(numero_de_disco, origem, destino, auxiliar):
    pass


def torre_de_hanoi(numero_de_disco: int):
    global contagem_de_chamdas_recusrivas
    contagem_de_chamadas_recursivas = 0
    _torre_de_hanoi_recursivo(numero_de_disco, origem='A', destino='B', auxiliar='C')


if __name__ == '__main__':
    torre_de_hanoi(1)
    torre_de_hanoi(2)