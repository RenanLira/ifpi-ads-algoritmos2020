cotacao_dolar = float(input('Digite o valor do dolar: R$ '))
valor_dolar = float(input('Digite um valor em dolar: $ '))

valor_real = valor_dolar * cotacao_dolar

print('O valor de $ {} para real é: R$ {}'.format(valor_dolar, valor_real))
