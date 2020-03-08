num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))

resto = num1 % num2
quociente = num1 // num2

print('Quociente da divisão({} / {}) é: {}\nResto da divisão({} / {}) é: {}'.format(num1, num2, quociente, num1, num2, resto))

