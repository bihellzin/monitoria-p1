print('Escolha uma das opções abaixo: ')
print('1. Entrar um valor W e um valor T e receber o valor total de watts consumidos.')
print('2. Entrar um valor W e um valor TOTAL e receber quanto tempo ficou no cômodo.')
print('3. Entrar um valor T e um valor TOTAL e receber quantos watts por minuto são consumidos no cômodo.')
opcao = int(input(''))

if opcao == 1:
    w = int(input('Insira os watts por minuto: '))
    t = int(input('Insira quantos minutos: '))

    print(w*t, 'watts foram consumidos')

elif opcao == 2:
    w = int(input('Insira os watts por minuto: '))
    total = int(input('Insira o watts totais consumidos: '))

    print('Você passou', total/w, 'minutos no cômodo')

elif opcao == 3:
    t = int(input('Insira quantos minutos: '))
    total = int(input('Insira o watts totais consumidos: '))

    print('O cômodo consome', total/t, 'watts por minutos')    

else:
    print('Essa opção não existe, programa fechado')