valor_produto = float(input('Digite o valor da mercadoria: '))

entrada = (valor_produto // 3) + (valor_produto % 3)
pretacoes = (valor_produto - entrada) / 2

print('Entrada: R$ {:.2f}\n2 pretações de: R$ {:.2f}'.format(entrada, pretacoes))