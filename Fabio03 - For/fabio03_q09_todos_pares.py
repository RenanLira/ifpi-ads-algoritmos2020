def main():
    limite_inferior = int(input('Informe o numero de começo: '))
    limite_superior = int(input('Informe o numero de termino: '))

    pares(limite_superior, limite_inferior)


def pares(ls, li):

    for i in range(li, ls+1):
        if i % 2 == 0:
            print(i)


main()