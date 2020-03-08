numero = int(input('Digite um numero de 3 digitos: '))

n3 = numero // 100
n2 = (numero % 100) // 10
n1 = (numero % 100) % 10

media = (n3 + n2 + n1) / 3

print('A media dos digitos é: {}'.format(media))