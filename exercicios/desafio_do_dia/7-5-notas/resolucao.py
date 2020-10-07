n = int(input('Insira a quantidade de alunos: '))
m = int(input('Insira a quantidade de listas: '))

historico = []
chocolates = 0

# Primeiro pegamos todas as notas
for i in range(n):
    notas = int(input('Insira a nota do aluno:'))

    notas_unicas = []
    for j in range(m):
        nota = notas % 10
        notas = notas // 10

        notas_unicas.append(nota)

    historico.append(notas_unicas)

# Depois vamos procurar a maior nota de cada lista
maiores_notas = []

for i in range(m):
    maior = 0
    for j in range(n):
        if historico[j][i] > maior:
            maior = historico[j][i]

    maiores_notas.append(maior)

for i in range(m):
    for j in range(n):
        if historico[j][i] == maiores_notas[i]:
            chocolates += 1

print(chocolates)
