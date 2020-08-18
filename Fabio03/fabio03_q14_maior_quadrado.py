def main():
    n = int(input('Digite um numero: '))

    print(f'O maior quadrado anterior a {n} é {maior_quadrado(n)}')


def maior_quadrado(n):
    quadrado = 0
    cont = 1
    while quadrado < n:
        quadrado = cont ** 2
        cont += 1

    if quadrado > n:
        quadrado = (cont-2) ** 2

    return quadrado


main()