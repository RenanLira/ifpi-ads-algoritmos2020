def main():
    n = int(input('Digite um numero: '))

    print(f'a soma de todos os numeros de 1 a {n} é {somar(n)}')


def somar(n):
    total = 0

    for i in range(n+1):
        total += i
    
    return total


main()