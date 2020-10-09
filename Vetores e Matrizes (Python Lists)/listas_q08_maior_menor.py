import functools


def main():
    lista = list(map(int, input('Numeros(separados por espaços): ').split()))

    maior = functools.reduce(lambda a, b: a if a > b else b, lista)
    print(f'Maior numero: {maior}, posição: {lista.index(maior)}')

    menor = functools.reduce(lambda a, b: a if a < b else b, lista)

    print(f'Menor numero: {menor}, posição: {lista.index(menor)}')


main()