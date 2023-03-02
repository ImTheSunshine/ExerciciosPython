nomes_notas = []
quantidade = 200
for _ in range(quantidade):
    nome = input('digite o nome:')
    nota = int(input('digite a nota:'))

    nomes_notas.append((nome, nota))

nomes_notas.sort(key=lambda t: t[1], reverse=True)
print(nomes_notas)