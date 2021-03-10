"""
Imprimir letra E na tela
"""

def latter_E(num):
    for row in range(num):
        if(row == 0 or row == num -1 or row == num//2):
            print('**********')
        else:
            print('*')
latter_E(7)
