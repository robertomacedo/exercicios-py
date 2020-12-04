# Slice first 5 list items


list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
result = slice(5)
print(list[result])


list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
result = slice(2, 7, 2)
print(list[result])


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
