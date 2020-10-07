'''
Escreva um programa que diz se
uma lista inserida está com todos
os seus elementos em ordem(crescente)
'''

lista = [1, 2, 3, 4, 5]

ordenado = True

for i in range(len(lista)-1):
    if lista[i] > lista[i+1]:
        ordenado = False

if ordenado:
    print('A lista esta ordenada')

else:
    print('A lista nao está ordenada')
