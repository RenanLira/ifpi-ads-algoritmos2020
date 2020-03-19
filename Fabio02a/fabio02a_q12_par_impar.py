def main():
    numero = int(input('Digite um numero: '))

    print('O numero {} é {}'.format(numero, impar_par(numero)))


def impar_par(num):
    if num % 2 == 0:
        return 'Par'

    elif num % 2 != 0:
        return 'Impar'


main()
    