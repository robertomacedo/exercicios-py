"""
Ache o segundo maior valor de um intervalo

A lista está ordenada
Se possui elementos duplicados

"""
from bisect import bisect_left
from numbers import Number
from typing import List


def encontrar_segundo_maior_valor_Lista_ordenada(lista_ordenada: List) -> Number:
    """
    >>> encontrar_segundo_maior_valor_Lista_ordenada([1, 1, 1, 1, 2, 2, 2, 3, 3, 3])
    2
    >>> encontrar_segundo_maior_valor_Lista_ordenada([1, 1, 1, 1, 2, 2, 2, 3, 3, 3,])
    2
    >>> encontrar_segundo_maior_valor_Lista_ordenada([1, 1, 1, 1, 2, 2, 2])
    1
    >>> encontrar_segundo_maior_valor_Lista_ordenada([1, 2])
    1
    >>> encontrar_segundo_maior_valor_Lista_ordenada([2, 2])
    2


    :param lista_ordenada:
    :return:
    """

    indice =bisect_left(lista_ordenada, lista_ordenada[-1])
    return lista_ordenada[indice-1]