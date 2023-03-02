lista = []
lista2 = []

for lt in range(30):
    lista.append(int(input(f'Digite o{lt+1}º número: ')))

for num in lista:
    if num % 2 == 0:
        lista2.append(num*2)
    else:
        lista2.append(num*3)

print(lista2)