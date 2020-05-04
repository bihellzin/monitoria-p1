n = int(input('Insira o quantidade de palavras: '))
cont = 0

while cont < n:
    palavra = input('Insira a palavra: ')

    if len(palavra) <= 10: # se o tamanho da palavra tiver 10 ou menos caracteres, ja printo a palavra
        print(palavra)

    else:
        saida = palavra[0] # adiciono a primeira letra da palavra na saida
        qntd_letras = 0
        for i in range(1, len(palavra)-1):
            qntd_letras = qntd_letras + 1 # percorro da segunda letra da palavra ate a penultima letra, mas eh possivel percorrer toda a palavra e subtrair 2

        saida = saida + str(qntd_letras) + palavra[-1] # adiciono a saida a string da variavel contendo a quantidade de letras entre a primeira e a ultima letra d palavr e depois adiciono a ultima letra

        print(saida)

    cont = cont + 1
