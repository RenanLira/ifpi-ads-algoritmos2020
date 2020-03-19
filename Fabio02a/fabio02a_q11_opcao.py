

def main():
    num1 = int(input('Digite um numero: '))
    num2 = int(input('Digite outro numero: '))
    num3 = int(input('Digite outro numero: '))
    opcao = int(input('Digite uma opção de 1 a 3: '))
    
    if verificar_opcao(opcao):
        print('Opcao invalida')


    print('O numero escolhido foi: {}'.format(escolher_num(opcao, num1, num2, num3)))

def verificar_opcao(opcao):
    if opcao > 3 or opcao < 1:
        return True

    return False 

def escolher_num(opcao, n1, n2, n3):
    if opcao == 1:
        return n1

    elif opcao == 2:
        return n2

    elif opcao == 3:
        return n3


main()