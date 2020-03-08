binario = int(input('Digite um valor em binario(4 digitos): '))

b4 = (binario // 1000) * 8
b3 = ((binario % 1000) // 100) * 4
b2 = (((binario % 1000) % 100) // 10) * 2
b1 = (((binario % 1000) % 100) % 10) * 1

decimal = b1 + b2 + b3 + b4

print('Em decimal é: {}'.format(decimal))