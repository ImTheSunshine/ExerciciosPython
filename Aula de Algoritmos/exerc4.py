from itertools import chain

A = [int(x) for x in input('Valores de "A": ').split()]
B = [int(x) for x in input('Valores de "B": ').split()]
C = list()
for item in chain(A, B):
    if (item in A) and (item in B) and (item not in C):
        C.append(item)
C.sort()
print(C)