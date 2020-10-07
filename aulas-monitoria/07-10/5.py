'''
Escreva um programa que procura o menor número numa lista
'''
import math

lista = [1, 2, 3, 4, 5, 6, 8, -3, -13, 8, -23, 15, 9]
menor = lista[0] # math.inf para certificar que vai ser o maior valor possível

for i in lista:
    if i < menor:
        menor = i

print(menor)
