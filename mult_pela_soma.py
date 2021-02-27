n = int(input('Digite o primeiro valor: '))
p = int(input('Digite o segundo valor: '))


def mult_pela_soma(n1, n2):

    """
    n1 = 2
    n2 = 4
    
    2 * 4 = 2 + 2 + 2 + 2
    mult_pela_soma(n1, n2)
    mult_pela_soma(n1, 0) = 0
    mult_pela_soma(n1, 1) = n1
    mult_pela_soma(n1, 2) = n1 + mult_pela_soma(n1, 2 - 1)
    mult_pela_soma(n1, 3) = n1 + mult_pela_soma(n1, 3 - 1)

    """
    if n1 == 0:
        return 0
    elif n2 == 1:
        return n1
    elif n2 < 0:
        return - mult_pela_soma(n1, -n2)  # resolve o case de entrada de um númeor negativo.
    else:
        return n1 + mult_pela_soma(n1, n2 - 1)


if __name__ == '__main__':
    print(mult_pela_soma(n, p))

#opc = int(input('Deseja continuar? \n1. Sim\n2. Sair\n'))
#if opc == 1:
#    mult_pela_soma(n, p)
#else:
#    print('Saindo...')

