def main():
    num1 = int(input('Digite um valor: '))
    num2 = int(input('Digite outro valor: '))

    resultado = calcular(num1, num2)
    print(resultado)

def calcular(n1, n2):
    if n1 % n2 == 1:
        return n1 + n2 + (n1 % n2)
    
    elif n1 % n2 == 2:
        valor1 = impar_par(n1)
        valor2 = impar_par(n2)
        return f'O primeiro valor é: {valor1}\nO segundo valor é: {valor2}'

    elif n1 % n2 == 3:
        return (n1 + n2) * n1

    elif n1 % n2 == 4:
        return (n1 + n2) / n2
    
    elif n1 % n2 == 0 or n1 % n2 > 4:
        quadrado1 = n1 ** (1/2)
        quadrado2 = n2 ** (1/2)
        
        return f'A raiz quadrada do valor 1 é: {quadrado1:0.2f}\nA raiz quadrada do valor 2 é: {quadrado2:0.2f}'

def impar_par(num):
    if num % 2 == 0:
        return 'Par'

    elif num % 2 != 0:
        return 'Impar'


main()