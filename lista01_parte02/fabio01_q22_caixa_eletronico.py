valor_saque = int(input('Digite o valor do saque: '))

nota_50 = valor_saque // 50
nota_10 = (valor_saque % 50) // 10
nota_5 = ((valor_saque % 50) % 10) // 5
nota_1 = ((valor_saque % 50) % 10) % 5

print('Notas sacadas:\nR$ 50: {}\nR$ 10: {}\nR$ 5: {}\nR$ 1: {}'.format(nota_50, nota_10, nota_5, nota_1))