def main():
    n = int(input('Digite um numero: '))

    print(f'a soma de todos os numeros de 1 a {n} é {somar(n)}')


def somar(n):
    total = 0
    cont = 1
    while cont <= n:
        total += cont
        cont += 1
    
    return total


main()