def main():
    angulo1 = int(input('Digite o 1° angulo: '))
    angulo2 = int(input('Digite o 2° angulo: '))
    angulo3 = int(input('Digite o 3° angulo: '))

    print(qual_triangulo(angulo1, angulo2, angulo3))


def qual_triangulo(angulo1, angulo2, angulo3):
    if eh_triangulo(angulo1, angulo2, angulo3) == True:
        return 'É um triangulo {}'.format(tipo_de_triangulo(angulo1, angulo2, angulo3))

    else:
        return 'Não é um triangulo'


def eh_triangulo(angulo1, angulo2, angulo3):
    return (angulo1 + angulo2 + angulo3) == 180


def tipo_de_triangulo(angulo1, angulo2, angulo3):
    if angulo1 == 90 or angulo2 == 90 or angulo3 == 90:
        return 'retangulo'

    elif angulo1 < 90 and angulo2 < 90 and angulo3 < 90:
        return 'acutângulo'

    elif angulo1 > 90 or angulo2 > 90 or angulo3 > 90:
        return 'obtusangulo'


main()