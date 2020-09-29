def main():
    n = int(input('Digite um numero: '))
    limite_superior = int(input('Informe o numero de termino: '))
    limite_inferior = int(input('Informe o numero de começo: '))

    multiplos(n, limite_superior, limite_inferior)


def multiplos(n, ls, li):
    print(f'Os multiplos de {n} de {li} a {ls} são:')
    multiplo = 0

    for i in range(li, ls):
        multiplo = n * i
        if multiplo > ls:
            break

        print(multiplo, end=' ')


main()