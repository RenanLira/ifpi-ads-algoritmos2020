def main():
    num = int(input('Escreva um numero: '))

    print(f'Este numero é {verificar_numero(num)}')


def verificar_numero(num):
    if num > 0:
        return 'positivo'

    elif num < 0:
        return 'negativo'

    else:
        return 'neutro'


main()