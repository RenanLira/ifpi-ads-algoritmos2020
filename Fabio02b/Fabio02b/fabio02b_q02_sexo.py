def main():
    print('Qual o seu sexo?\nF - Feminino\nM - Masculino')
    letra = input('-> ').upper()

    print(verificar_sexo(letra))


def verificar_sexo(letra):
    if letra == 'F':
        return 'Feminino'

    elif letra == 'M':
        return 'Masculino'

    else:
        return 'Sexo invalido'


main()