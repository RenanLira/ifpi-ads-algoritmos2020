def main():
    numero = int(input('Digite um numero de 4 digitos: '))

    if verificar_caracteristica(numero):
        print('Este numero obedesce a caracteristica')

    else:
        print('Este numero não obedesce a caracteristica')


def verificar_caracteristica(numero):
    parte1 = numero // 100
    parte2 = numero % 100

    novo_num = parte1 + parte2
    novo_num = novo_num ** 2

    if novo_num == numero:
        return True

    else:
        return False 


main()