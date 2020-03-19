def main():
    lado_1 = int(input('Digite o primeiro lado do triangulo: '))
    lado_2 = int(input('Digite o segundo lado do triangulo: '))
    lado_3 = int(input('Digite o terceiro lado do triangulo: '))

    print(qual_triagulo(lado_1, lado_2, lado_3))


def eh_triangulo(lado_1, lado_2, lado_3):
    return (lado_1 + lado_2) > lado_3 and (lado_1 + lado_3) > lado_2 and (lado_3 + lado_2) > lado_1


def tipo_triangulo(lado_1, lado_2, lado_3):
    if lado_1 == lado_2 and lado_2 == lado_3:
        return 'equilátero'

    elif lado_1 == lado_2 or lado_1 == lado_3 or lado_2 == lado_3:
        return 'isósceles'

    else:
        return 'escaleno'


def qual_triagulo(lado_1, lado_2, lado_3):
    if eh_triangulo(lado_1, lado_2, lado_3) == True:
        return 'É um triangulo {}'.format(tipo_triangulo(lado_1, lado_2, lado_3))
    else:
        return 'Não é um triangulo'


main()