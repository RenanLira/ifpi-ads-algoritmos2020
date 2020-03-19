
def main():
    numero1 = int(input('Digite um numero: '))
    numero2 = int(input('Digite outro numero: '))
    numero3 = int(input('Digite outro numero: '))

    resultado = comparador(numero1, numero2, numero3)

    print(resultado)


def comparador(num1, num2, num3):
    if num1 == num2 and num2 == num3:
        return 'todos os numeros são iguais'
    elif num1 != num2 and num2 != num3 and num1 != num3:
        return 'não há nenhum numero igual'
    elif num1 == num2 or num2 == num3 or num1 == num3:
        return 'há 2 numeros iguais'

main() 