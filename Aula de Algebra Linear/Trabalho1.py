# Usuario digita a matriz
print("Digite os dados da matriz 4x4 (16 números):")

# Matriz sera 4x4
 
A44 = [[0 for j in range(4)] for i in range(4)]

#Looping para o usuario digitar a matriz completa
for i in range(4):
    for j in range(4):
        A44[i][j] = float(input(f"Digite o valor de A[{i+1}][{j+1}]: "))

#Mostrando resultado da matriz

print("A = [")
for i in range(4):
    print("  ", end="")
    for j in range(4):
        print(f"{A44[i][j]:.0f}", end=" ")
    print("")
print("]")

# Obtendo a matriz A superior 
Asuperior = [[0 for j in range(4)] for i in range(4)]
for i in range(4):
    for j in range(4):
        if i <= j:
            Asuperior[i][j] = A44[i][j]



# Imprimindo a matriz A superior
print("Asuperior = [")
for i in range(4):
    print("  ", end="")
    for j in range(4):
        print(f"{Asuperior[i][j]:.0f}", end=" ")
    print("")
print("]")

# Obtendo a matriz A inferior 
Ainferior = [[0 for j in range(4)] for i in range(4)]
for i in range(4):
    for j in range(4):
        if i >= j:
            Ainferior[i][j] = A44[i][j]

# Imprimindo a matriz A inferior
print("Ainferior = [")
for i in range(4):
    print("  ", end="")
    for j in range(4):
        print(f"{Ainferior[i][j]:.0f}", end=" ")
    print("")
print("]")