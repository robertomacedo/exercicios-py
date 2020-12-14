"""
Busca sequecial em um vetor

"""

def buscar_elemento(v, x):
    i = 0
    while i < len(v):
        if v[i] == x:
            return i
        i += 1
    return -1

vetor = list(range(0, 100))
print(vetor)