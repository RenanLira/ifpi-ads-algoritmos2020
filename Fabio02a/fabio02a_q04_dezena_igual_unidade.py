def main():
    numero = int(input('Digite um numero de 2 digitos: '))

    print(comparacao(numero))

    
def comparacao(numero):
    dezena = numero // 10
    unidade = numero % 10

    if dezena == unidade:
        return 'A dezena é igual a unidade'

    else:
        return 'A dezena e a unidade são diferentes'


main()
