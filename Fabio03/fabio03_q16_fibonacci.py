def main():
    n = int(input('Digite o tamanho da sequencia: '))

    fibonacci(n)


def fibonacci(n):
    cont = 0
    ant = 0
    result = 1
    while cont < n:
        print(result)
        result += ant
        ant = result - ant

        cont += 1





main()