import sys
import string
import time
from itertools import combinations_with_replacement
from datetime import timedelta
from random import random, choice
"""
Gerador de senha 
O programa recebe números, letras mais caracteres espciais 
e gera as combinações possíveis para gerar senhas com as combinações possíveis.
"""

def main(args):
    values = string.ascii_letters
    values += string.digits
    values += string.punctuation
    tamanho = 3

    ini_t = time.time()
    gerar_senhas(values, tamanho)
    fin_t = time.time()

    print("Tempo: " + str(fin_t - ini_t))


def gerar_senhas(values, tamanho):
    comb = combinations_with_replacement(values, tamanho)
    print("Combinacoes: " + str(len(list(comb))))


if __name__ == "__main__":
    main(sys.argv[1:])
