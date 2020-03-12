n = int(input('Digite o número que deseja saber o fatorial: '))

fatorial = 1

while n > 1:
    fatorial = fatorial * n
    n = n -1

print(fatorial)