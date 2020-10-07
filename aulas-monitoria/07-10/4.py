'''
Escreva um programa que recebe uma lista e conta quantas
vezes um elemento se repete nela.
'''

lista = [1, 2, 3, 1, 4, 1, 5, 1]

elemento = int(input('Insira o valor do elemento: '))
cont = 0

for i in lista:
    if i == elemento:
        cont += 1

print(f'O elemento {elemento} foi encontrado {cont} vezes na lista')
