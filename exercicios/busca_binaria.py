"""
max([1, 4, 2, 5])       O(n)
min([1, 4, 2, 5])       O(n)
mediana([1, 4, 2, 5])   O(n log(n))
busca([1, 4, 2, 5])


max([1, 4, 2, 5])       O(1)
min([1, 4, 2, 5])       O(1)
mediana([1, 4, 2, 5])   O(1)
busca([1, 4, 2, 5])     O(?)

[0, 200] idade 100 não <
[0, 99] idade 50 não <
[0, 49] idade 25 não >
[26, 49] idade 37 não >
[38, 49] idade 43 não >
[44, 49] idade 46 não <
[44, 45] idade 44 sim

a(0) = n
a(1) = n / 2
a(2) = n / 4
a(3) = n / 8
...
...
a(i = n / 2 ** i
a(i) <= 1

<=>

n / 2 ** i <= 1

=>

lg(n / 2 ** i) <= lg(1) =>

lg(n) - lg(2 ** i) <= 0 =>

lg(n) <= i

"""


def bissecao_baixa(lista_ordenada: list, elemento: int):
    """
    >>> bissecao_baixa([], -1)
    0
    >>> bissecao_baixa([-1], 1)
    1
    >>> bissecao_baixa([-1, 1], 2)
    2
    >>> bissecao_baixa([-1, 1], -2)
    0
    >>> bissecao_baixa([-1, 1], 0)
    1
    >>> bissecao_baixa([-1, 1, 2], 0)
    1


    :param lista_ordenada:
    :param elemento:
    :return:
    """

    indice_inicial = 0
    indice_final = len(lista_ordenada) -1
    n = len(lista_ordenada)
    if indice_final < indice_inicial:
        return indice_inicial
    elif n == 1:
        elemento_do_meio = lista_ordenada[0]
        if elemento < elemento_do_meio:
            return 0
        return 1
    elif n == 2:
        elemento_do_meio = lista_ordenada[0]
        if elemento < elemento_do_meio:
            return 0
        elemento_do_meio = lista_ordenada[1]
        if elemento < elemento_do_meio:
            return 1
        return 2
    elif n == 3: # [-1, 1, 2], 0
        elemento_do_meio = lista_ordenada[1] #1
        if elemento < elemento_do_meio: # indice_inicial = 0
            elemento_do_meio = lista_ordenada[0]
            if elemento < elemento_do_meio:
                return 0
            return 1
        elemento_do_meio = lista_ordenada[1]
        if elemento < elemento_do_meio:
            return 1
        return 2
    return 2