def main():
    print('Digite os preços dos produtos abaixo')
    produto1 = float(input('Produto 1 R$: '))
    produto2 = float(input('Produto 2 R$: '))
    produto3 = float(input('Produto 3 R$: '))

    print(f'O produto a ser escolhido é o {verificar_produto(produto1, produto2, produto3)}')


def verificar_produto(produto1, produto2, produto3):
    menor_valor = mais_barato(produto1, produto2, produto3)
    if produto1 == menor_valor:
        return 'produto 1'

    elif produto2 == menor_valor:
        return 'produto 2'

    elif produto3 == menor_valor:
        return 'produto 3'

    else:
        return 'hmmm'


def mais_barato(produto1, produto2, produto3):
    menor = mais_caro(produto1, produto2, produto3)
    for i in produto1, produto2, produto3:
        if menor > i:
            menor = i

    return menor


def mais_caro(produto1, produto2, produto3):
    maior = 0
    for i in produto1, produto2, produto3:
        if maior < i:
            maior = i

    return maior
    
main()