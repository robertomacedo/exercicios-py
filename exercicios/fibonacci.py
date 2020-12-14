"""
Lógica usando a sequência de Fibonacci
"""

def fibo():
    pass

anterior = 0
proximo = 1
s = 1


for n in range(0, 101):
    print(anterior)         #Início do valor em zero;
    s = proximo + anterior  #s é a soma do número atual mais o anterior no caso 1 + 0;
    anterior = proximo      #Anterior agora recebe o valor de proximo no caso valor 1
    proximo = s             #
print(n)