def main():
    n = int(input('Digite o tamanho da sequencia: '))

    sequencia(n)


def sequencia(n):
    n_seq = 1
    for i in range(1, n):
        print(n_seq, end=" ")
        n_seq += i+1


main()