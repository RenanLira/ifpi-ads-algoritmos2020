numero = int(input('Digite um numero de 3 digitos: '))

centena = numero // 100
dezena = (numero % 100) // 10
unidade = numero % 10
numero_inverso = str(unidade) + str(dezena) + str(centena)
numero_inverso = int(numero_inverso)

print('O numero inverso é: {}'.format(numero_inverso))