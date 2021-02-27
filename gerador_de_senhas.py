import sys
import string
import time
from itertools import combinations_with_replacement
from datetime import timedelta
from random import random, choice
"""
Gerador de senha 
O programa recebe números, letras e caracteres especiais 
para gerar combinações possíveis e apresenta o total de resultados
e o tempo gasot para executar a tarefa.

O tempo é proporcional ao número de caracteres
"""

print('============================================')
print('GERADOR DE SENHAS USANDO PYTHON')

tamanho = int(input('Digite um número: '))
def main(args):
    values = string.ascii_letters
    values += string.digits
    values += string.punctuation
    #tamanho = ''

    ini_t = time.time()
    gerar_senhas(values, tamanho)
    fin_t = time.time()

    print(f'O tempo de processo toral foi de: ' + str(fin_t - ini_t), 'segundos')


def gerar_senhas(values, tamanho):
    comb = combinations_with_replacement(values, tamanho)
    print(f'Número de combinações em uma senha de {tamanho} digitos é: ' + str(len(list(comb))))


if __name__ == "__main__":
    main(sys.argv[1:])
