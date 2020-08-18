def main():
    n = int(input('Digite o tamanho da sequencia: '))

    sequencia(n)


def sequencia(n):
    cont = 1
    n_seq = 1
    while cont < n:
        print(n_seq, end=' ')
        cont += 1
        n_seq += cont


main()