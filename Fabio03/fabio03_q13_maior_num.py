def main():
    n = int(input('Digite o tamanho da lista: '))

    maior_num = info_lista(n)
    print(f'O maior numero da lista é {maior_num}')


def info_lista(n):
    cont = 0
    num_a = 0
    while cont < n:
        num = int(input('Digite um numero da lista: '))

        if num > num_a:
            num_a = num

        cont += 1

    return num_a


main()