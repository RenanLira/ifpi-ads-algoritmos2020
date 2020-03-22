def main():
    numero = int(input('Digite um numero(menor que 1000): '))

    print(forma_frase(numero))
    

def forma_frase(numero):
    centena = pegar_centena(numero)
    dezena = pegar_dezena(numero)
    unidade = pegar_unidade(numero)

    quantidade = 3
    for i in centena, dezena, unidade:
        if i == ' ':
            quantidade -=1

    if quantidade == 3:
        return f'{centena}, {dezena} e {unidade}'

    elif quantidade == 2:
        return f'{dezena} e {unidade}'

    elif quantidade == 1:
        return f'{unidade}'

    else:
        return 'Valor invalido'


def pegar_centena(numero):
    cent = numero // 100
    if cent > 1:
        nome = 'centenas'
    elif cent == 1:
        nome = 'centena'

    else:
        cent = ''
        nome = ''
    
    return f'{cent} {nome}' 


def pegar_dezena(numero):
    deze = (numero % 100) // 10
    if deze > 1:
        nome = 'dezenas'
    elif deze == 1:
        nome = 'dezena'

    else:
        deze = ''
        nome = ''
    
    return f'{deze} {nome}' 


def pegar_unidade(numero):
    uni = (numero % 100) % 10
    if uni > 1:
        nome = 'unidades'
    elif uni == 1:
        nome = 'unidade'

    else:
        uni = ''
        nome = ''
    
    return f'{uni} {nome}'


main()