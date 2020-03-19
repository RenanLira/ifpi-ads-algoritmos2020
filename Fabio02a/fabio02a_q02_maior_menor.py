def main():
    num1 = int(input('Digite um numero: '))
    num2 = int(input('Digite outro numero: '))

    resultado = maior_menor(num1, num2)

    print(resultado)


def maior_menor(num1, num2):
    if num1 > num2:
        return 'Maior: {}\nMenor: {}'.format(num1, num2)

    elif num2 > num1:
        return 'Maior: {}\nMenor: {}'.format(num2, num1)

    else:
        return 'Os numeros são iguais'


main()