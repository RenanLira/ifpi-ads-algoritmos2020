def main():
    angulo = int(input('Digite um angulo: '))

    if quadrante(angulo):
        print(f'O angulo {angulo} pertence ao {quadrante(angulo)} quadrante')

    else:
        print('Angulo invalido')


def quadrante(angulo):
    if angulo > 0 and angulo < 90:
        return 'primeiro'

    elif angulo > 90 and angulo < 180:
        return 'segundo'

    elif angulo > 180 and angulo < 270:
        return 'terceiro'

    elif angulo > 270 and angulo < 360:
        return 'quarto'

    elif angulo == 90 or angulo == 180 or angulo == 270 or angulo == 360:
        return 'fora de'

    else:
        return False


main()