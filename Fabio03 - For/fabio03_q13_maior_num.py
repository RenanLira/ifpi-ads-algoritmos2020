def main():
    n = int(input('Digite o tamanho da lista: '))

    maior_num = info_lista(n)
    print(f'O maior numero da lista é {maior_num}')


def info_lista(n):
    num_a = 0
    for i in range(n):
        num = int(input('Digite um numero da lista: '))

        if num > num_a:
            num_a = num

    return num_a


main()