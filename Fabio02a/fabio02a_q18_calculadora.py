def main():
    num1 = float(input('Digite um numero: '))
    num2 = float(input('DIgite outro numero: '))
    print('Escolha uma opção:')
    print('1 – Adição\n2 – Subtração\n3 – Multiplicação\n4 – Divisão')
    opcao = int(input('-> '))

    resultado = verificar_opcao(opcao, num1, num2)

    if resultado:
        print(f'O resultado é: {resultado}')
    else:
        print('Opção invalida')

        
def verificar_opcao(opcao, num1, num2):
    if opcao == 1:
        return calcular_adicao(num1, num2)
    
    elif opcao == 2:
        return calcular_subtracao(num1, num2)
    
    elif opcao == 3:
        return calcular_multiplicacao(num1, num2)
    
    elif opcao == 4:
        return calcular_divisao(num1, num2)
    
    else:
        return False


def calcular_adicao(num1, num2):
    return num1 + num2


def calcular_subtracao(num1, num2):
    return num1 - num2


def calcular_multiplicacao(num1, num2):
    return num1 * num2


def calcular_divisao(num1, num2):
    return num1 / num2


main()