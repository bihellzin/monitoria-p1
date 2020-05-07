ano = int(input('Insira o ano: '))
ano_seguinte = ano + 1

algum_igual = True

while algum_igual:
    aux = ano_seguinte
    digito1 = aux // 1000
    aux = aux % 1000

    digito2 = aux // 100
    aux = aux % 100

    digito3 = aux // 10
    aux = aux % 10

    digito4 = aux

    if digito1 != digito2 and digito1 != digito3 and digito1 != digito4 and digito2 != digito3 and digito2 \
            != digito4 and digito3 != digito4:
        print(ano_seguinte)
        algum_igual = False

    ano_seguinte = ano_seguinte + 1
