def main():
    print('Digite a letra correspondente ao seu turno')
    print('M - Matutino\nV - Vespertino\nN - Noturno')
    turno = input('-> ').upper()

    print(verificar_turno(turno))


def verificar_turno(turno):
    if turno == 'M':
        return 'Bom Dia!'

    elif turno == 'V':
        return 'Boa Tarde!'

    elif turno == 'N':
        return 'Boa Noite!'

    else:
        return 'Valor Invalido'


main()