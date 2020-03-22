def main():
    numero = int(input('Digite um numero: '))

    print(verificar_dia(numero))


def verificar_dia(numero):
    contador = 1
    for i in 'domingo', 'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sabado':
        if contador == numero:
            return i
        contador += 1


main()