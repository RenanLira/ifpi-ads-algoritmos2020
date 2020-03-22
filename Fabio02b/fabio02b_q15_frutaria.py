def main():
    qtd_morango = int(input('Total de morangos(kg): '))
    qtd_macas = int(input('Total de maças(kg): '))

    total_a_pagar = calcular_preco_total(qtd_macas, qtd_morango)

    print('-'*30)
    print(f'Total a pagar: R$ {total_a_pagar}')


def calcular_preco_total(qtd_macas, qtd_morango):
    preco_morango = calcular_valor_morango(qtd_morango)
    preco_maca = calcular_valor_maca(qtd_macas)

    preco_total = (preco_maca * qtd_macas) + (preco_morango * qtd_morango)
    if preco_total > 25 or qtd_macas + qtd_morango > 8:
        desconto_total = (10/100) * preco_total

    else:
        desconto_total = 0

    return preco_total - desconto_total


def calcular_valor_morango(qtd_morango):
    preco = 0
    if qtd_morango <= 5:
        preco = 2.5

    elif qtd_morango > 5:
        preco = 2.2

    return preco


def calcular_valor_maca(qtd_macas):
    preco = 0
    if qtd_macas <= 5:
        preco = 1.8

    elif qtd_macas > 5:
        preco = 1.5

    return preco


main()