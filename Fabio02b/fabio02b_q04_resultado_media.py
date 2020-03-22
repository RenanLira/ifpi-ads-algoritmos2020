def main():
    nota1 = float(input('Digite a primeira nota do aluno: '))
    nota2 = float(input('Digite a segunda nota do aluno: '))

    print(f'O aluno foi {verificar_resultado(nota1, nota2)}!')


def verificar_resultado(nota1, nota2):
    media = calcular_media(nota1, nota2)

    if media >= 7:
        if media == 10:
            return 'aprovado com distinção'
        else:
            return 'aprovado'

    elif media < 7:
        return 'reprovado'


def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2


main()