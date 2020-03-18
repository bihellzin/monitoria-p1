n = input('Insira o valor de N: ')

soma = 0

for i in range(len(n)):
    soma = soma + (int(n) % 10)
    n = n[:-1]

print(soma)
