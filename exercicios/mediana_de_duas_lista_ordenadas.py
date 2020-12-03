from numbers import Number


def mediana_de_duas_listas(a: list, b: list) -> Number:
    """
    >>> mediana_de_duas_listas([1], [])
    1
    >>> mediana_de_duas_listas([1], [2])
    1.5
    >>> mediana_de_duas_listas([1], [2, 3000])
    2
    >>> mediana_de_duas_listas([1, 3], [2, 3000])
    2.5

    :param a:
    :param b:
    :return:
    """

    lista_concatenada = a + b
    return mediana(lista_concatenada)


def mediana(lista: list) -> Number:
    """
    >>> mediana([1])
    1
    >>> mediana([1, 2])
    1.5
    >>> mediana([1, 2, 3])
    2

    Complexidade de tempo de execução: O((n+m)log(n+n))
    Complexidade de memória: O(n+m)

    :param lista:
    :return:
    """

    # Algoritimo do elemento do meio de uma lista

    lista.sort()
    tamanho = len(lista)

    indice_do_elemento_do_meio = tamanho // 2
    if tamanho % 2 == 1:
        return lista[indice_do_elemento_do_meio]
    return (lista[indice_do_elemento_do_meio] + lista[indice_do_elemento_do_meio - 1]) / 2
