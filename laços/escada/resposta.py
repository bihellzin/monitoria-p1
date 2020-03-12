n = int(input('Insira a quantidade de degraus: '))

jogo_da_velha = '#'
espacos = ' '

cont = 1

while cont <= n:
    print(espacos * (n - cont) + (jogo_da_velha * cont))
    cont += 1