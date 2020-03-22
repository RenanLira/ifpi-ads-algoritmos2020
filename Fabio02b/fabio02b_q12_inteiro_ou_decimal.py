def main():
    numero = float(input('Digite um numero(inteiro ou decimal): '))

    print(f'Este numero é {verificar_numero(numero)}')


def verificar_numero(numero):
    num_int = int(numero)
    if numero / num_int == 1:
        return 'inteiro'
    else:
        return 'decimal'


main()