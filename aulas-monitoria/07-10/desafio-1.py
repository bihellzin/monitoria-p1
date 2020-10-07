lista = [4, 3, 2, 1, 5]

for i in range(len(lista)-1):
    elemento = lista[0]
    for j in range(1, len(lista)):
        if elemento > lista[j]:
            temp = lista[j]
            lista[j] = elemento
            lista[j-1] = temp
            

print(lista)
