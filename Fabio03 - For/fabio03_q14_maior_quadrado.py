def main():
    n = int(input('Digite um numero: '))

    print(f'O maior quadrado anterior a {n} é {maior_quadrado(n)}')


def maior_quadrado(n):
    quadrado = 0
    for i in range(n):
        quadrado = i ** 2
        if quadrado > n:
            quadrado = (i-1) ** 2
            break

    return quadrado


main()