numero = int(input('Digite um numero inteiro de 3 digitos: '))

centena = numero // 100
dezena = (numero % 100) // 10
unidade = ((numero % 100) % 10)

soma = centena + dezena + unidade

print('A soma dos elementos(C + D + U) do numero {} é: {}'.format(numero, soma))