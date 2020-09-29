def main():
    n = int(input('Digite o tamanho da sequencia: '))

    fibonacci(n)


def fibonacci(n):
    ant = 0
    result = 1

    for i in range(n):
        print(result)

        result += ant
        ant = result - ant






main()