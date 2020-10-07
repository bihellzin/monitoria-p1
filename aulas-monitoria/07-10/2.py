'''
Escreva um programa que receba uma lista de listas
de números inteiros e imprima a soma dos elementos de cada
lista
'''
lista = [[1, 2, 3], [4, 5, 6], [10, 11]]

for i in range(len(lista)):
    soma = 0
    for j in range(len(lista[i])):
        soma += lista[i][j]
    print(soma)
