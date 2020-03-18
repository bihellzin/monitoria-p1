n = int(input('Insira o valor de N: '))
soma = 0

while n != 0:
    soma += n % 10 # soma = soma + n % 10
    n //= 10 # n = n // 10

print(soma)
