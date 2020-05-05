n = int(input('Insira a quantidade de desafios: '))
desafios_resolvidos = 0

for i in range(n):
    guilherme = int(input('Guilherme sabe ? '))
    roseno = int(input('Roseno sabe ? '))
    pedro = int(input('Pedro sabe ? '))

    if guilherme + roseno + pedro >= 2:
        desafios_resolvidos = desafios_resolvidos + 1

print(desafios_resolvidos)
