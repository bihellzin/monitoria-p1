contador_corretas = 0
contador_incorretas = 0
contador = 0

print('1. Quantos dias tem um ano bissexto ? ')
resposta1_correta = 366
resposta1_usuario = int(input(''))

if resposta1_correta == resposta1_usuario:
    print('Você acertou a pergunta')
    contador_corretas += 1

else:
    print('Você errou a pergunta')
    contador_incorretas += 1

contador += 1

print('')
print('Até o momento, vc acertou %d, errou %d, de %d perguntas respondidas' %(contador_corretas, contador_incorretas, contador))
print('')

print('2. Qual a capital de Rondônia ? ')
resposta2_correta = 'Porto Velho'
resposta2_usuario = input('')

if resposta2_correta == resposta2_usuario:
    print('Você acertou a pergunta')
    contador_corretas += 1


else:
    print('Você errou a pergunta')
    contador_incorretas += 1

contador += 1


print('')
print('Até o momento, vc acertou %d, errou %d, de %d perguntas respondidas' %(contador_corretas, contador_incorretas, contador))
print('')


print('3. Em que ano o Brasil perdeu de 7x1 ? ')
resposta3_correta = 2014
resposta3_usuario = int(input(''))

if resposta3_correta == resposta3_usuario:
    print('Você acertou a pergunta')
    contador_corretas += 1


else:
    print('Você errou a pergunta')
    contador_incorretas += 1

contador += 1


print('')
print('Até o momento, vc acertou %d, errou %d, de %d perguntas respondidas' %(contador_corretas, contador_incorretas, contador))
print('')
