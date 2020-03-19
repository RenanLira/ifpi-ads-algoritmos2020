def main():
    nota1 = float(input('Digite a primeira nota do aluno: '))
    nota2 = float(input('Digite a segunda nota do aluno: '))
    media = calcular_media(nota1, nota2)

    if media < 7:
        print(f'Sua media é: {media:0.1f}')
        nota3 = float(input('Digite a nota final do aluno: '))
        media_final = calcular_media(nota1, nota2, nota3)

        if media_final < 5:
            print(f'Sua media é: {media_final:0.1f}')
            print('Reprovado')
        else:
            print(f'Sua media é: {media_final:0.1f}')
            print('Aprovado')
    else:
        print(f'Sua media é: {media:0.1f}')
        print('Aprovado')


def calcular_media(nota1, nota2, nota3=11):
    soma = 0
    for i in nota1, nota2, nota3:
        soma += i

    if nota3 == 11:
        return (soma - 11) / 2

    else:
        return soma / 3


main()