"""
Exemplo para estudar a lógica em um algorítmo de recursão
entendendo que ela é muito usada para navegar em árvores de estrutura de dados

"""
import os


def escanear_pastas(pasta_inicial, pasta = '', nivel = 0):
    """
    #>>> listar todos os arquivos de uma pasta
    :param pasta_inicial: caminho passado para ser listado
    :param pasta:
    :param nivel:
    :return:
    """
    # Código navega em todas as pastas no caminho que for passado.
    caminho = os.path.join(pasta_inicial, pasta)
    if not os.path.isdir(caminho):
        return
    arquivos = os.listdir(caminho)

    for arquivo in arquivos:
        print('\t' * nivel, '>', arquivo)
        escanear_pastas(caminho, arquivo, nivel + 1) # Na variável arquivo estamos rebendo apenas os nomes dos arquivos e pasta dentro do caminho passado

caminho = '/home/roberto/Documentos'
escanear_pastas(caminho)