def main():
    n = int(input('Digite o tamanho da lista: '))

    soma, media = info_lista(n)
    print(f'A soma dos itens da lista é {soma} e a media é {media}')


def info_lista(n):
    cont = 0
    soma_num = 0
    media = 0
    while cont < n:
        num = int(input('Digite um numero da lista: '))

        soma_num += num

        cont += 1

    media = soma_num / n

    return soma_num, media


main()