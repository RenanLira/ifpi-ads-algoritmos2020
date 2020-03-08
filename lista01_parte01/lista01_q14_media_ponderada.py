nota1 = float(input('Digite a primeira nota do aluno: '))
peso1 = int(input('Digite o peso da nota: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
peso2 = int(input('Digite o peso da nota: '))
nota3 = float(input('Digite a terceira nota do aluno: '))
peso3 = int(input('Digite o peso da nota: '))

media_ponderada = ((nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3)) / (peso1 + peso2 + peso3)

print('A media desse aluno é: {}'.format(media_ponderada))