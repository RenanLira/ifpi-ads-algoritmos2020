numero = int(input('Digite um numero de 4 digitos: '))

n4 = numero // 1000
n3 = (numero % 1000) // 100
n2 = (numero % 100) // 10
n1 = (numero % 100) % 10

soma = n4 + n3 + n2 + n1

print('A soma dos elementos do numero {} é: {}'.format(numero, soma))