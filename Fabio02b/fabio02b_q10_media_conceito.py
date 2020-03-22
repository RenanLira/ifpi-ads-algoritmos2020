def main():
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))

    aprovacao = verificar_aprovacao(nota1, nota2)

    print('-'*30)
    print(f'Nota 1: {nota1}')
    print(f'Nota 2: {nota2}')
    print(f'Media: {calcular_media(nota1, nota2)}')
    print(f'Conceito: {conceito(calcular_media(nota1, nota2))}')
    print('-'*30)
    print(aprovacao)
    print('-'*30)


def verificar_aprovacao(nota1, nota2):
    media = calcular_media(nota1, nota2)

    letra = conceito(media)

    if letra == 'A' or letra == 'B' or letra == 'C':
        return 'APROVADO'

    elif letra == 'D' or letra == 'E':
        return 'REPROVADO'

    else:
        return 'Erro Inesperado'


def conceito(media):

    if media >= 9 and media <= 10:
        return 'A'

    elif media >= 7.5 and media < 9:
        return 'B'

    elif media >= 6 and media < 7.5:
        return 'C'

    elif media >= 4 and media < 6:
        return 'D'
    
    elif media >= 0 and media < 4:
        return 'E'

    else:
        return 'ERROR'


def calcular_media(n1, n2):
    return (n1 + n2) / 2


main()