# Slice first 5 list items


list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
result = slice(2, 7)
print(list[result]) #Imprime como resul [a,b,c,d,e]


list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
result = slice(2, 7, 2) #Imprime os elementos [c, e, g] o número 2 indica o primeiro elemento
print(list[result])     #o número 7 indica o elemento de parada da chamada, ou seja, o índice 6
                        # o 2 no final repesenta os passos pulando de dois em dois os indices.

# Slice with negative indeces
list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
result = slice(-7, -2)
print(list[result])


#Reverse a sequence
# We can reverse a sequence by speciting both start and stop indices as none a step as -1
list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
result = slice(None, None, -1)
print(list[result])


# enumerate exemples
L = ['red', 'green', 'blue', 'amend']
for pair in enumerate(L):
    print(pair)

x = complex(3, 2)
print(x)


#Função cria lista dentro de lista;
def add_lista(list_num):
    resultado = []
    for n in list_num:
        resultado.append([x for x in range(1, n + 1) if n % x == 0])
    return resultado
print(add_lista([3, 4, 6]))


frase = 'A B C D e F g H i j'
new = []
for i in frase.split():
    if i.isupper():
        new.append(i)

print(new)