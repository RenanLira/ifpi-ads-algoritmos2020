def main():
    numero = int(input('Digite um numero de 4 digitos: '))

    if quadrado_perfeito(numero):
        print(f'O numero {numero} é um quadrado perfeito!')

    else:
        print(f'O numero {numero} não é um quadrado perfeito')


def quadrado_perfeito(numero):
    raiz_quadrada = numero ** (1/2)
    dezena1 = numero // 100
    dezena2 = numero % 100

    if dezena1 + dezena2 == raiz_quadrada:
        return True

    else:
        return False


main()