numero = int(input('Digite um numero de 3 digitos: '))

n3 = str(numero // 100)
n2 = str((numero % 100) // 10)
n1 = str((numero % 100) % 10)

num_inverso = int(n1 + n2 + n3)

resultado = numero + num_inverso

print('{} + {} = {}'.format(numero, num_inverso, resultado))