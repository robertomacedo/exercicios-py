"""
Escada de palavra

https://www.programcreek.com;2012/12/leetcode-word-ladder/

"""

def tamanho_sequencia_transformacao(inicio: str, palavra_final: str, dicionario: set) -> int:
    """
    >>> tamanho_sequencia_transformacao('dog', 'cog', {"hot", "dot", "dog", "lot", "log"})
    True
    >>> tamanho_sequencia_transformacao('dig', 'cog')
    False
    :param inicio:
    :param palavra_final:
    :param dicionario:
    :return:
    """
    palavra_corrente = inicio

    if possui_apenas_uma_letra_diferente(palavra_corrente, palavra_final):
        pass

def possui_apenas_uma_letra_diferente(palavra: str, outra_palavra: str) -> bool:
    """

    :param palavra:
    :param outra_palavra:
    :return:
    """
