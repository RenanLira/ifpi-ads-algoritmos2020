def main():
    print('Tipo de carne: ')
    print('A - Alcatra\nF - File\nP - Picanha')
    tipo_de_carne = input('-> ').upper()
    qtd_carne = float(input('Quantidade(kg): '))
    print('-'*30)
    print('Forma de Pagamento')
    print('1 - Cartão Tabajara\n2 - Dinheiro\n3 - Cartão de Credito/Debito')
    forma_pag = int(input('-> '))

    if verificar_erros(tipo_de_carne, qtd_carne, forma_pag):
        print(nota_fiscal(tipo_de_carne, qtd_carne, forma_pag))
    
    else:
        print('Erro no sistema(Valores inserido invalido)')


def verificar_erros(tipo_de_carne, qtd_carne, forma_pag):
    if tipo_de_carne != 'A' and tipo_de_carne != 'F' and tipo_de_carne != 'P':
        return False

    if qtd_carne <= 0:
        return False

    if forma_pag > 3 or forma_pag < 1:
        return False

    return True


def nota_fiscal(tipo_de_carne, qtd_carne, forma_pag):
    preco_final, preco_total, desconto_cartao, tipo = total_a_pagar(tipo_de_carne, qtd_carne, forma_pag)
    tipo_pag = ''

    if forma_pag == 1:
        tipo_pag = 'Cartão Tabajara'

    elif forma_pag == 2:
        tipo_pag = 'Dinheiro'

    elif forma_pag == 3:
        tipo_pag = 'Cartão de credito/Debito'

    p1 = 'Tipo de carne:'
    p2 = 'Quantidade:'
    p3 = 'Preco Total:'
    p4 = 'Tipo de Pagamento:'
    p5 = 'Valor do desconto:'
    p6 = 'TOTAL A PAGAR:'

    traco = '-'*50    
    p1_t = p1 + ' '*(25 - len(p1)) + tipo
    p2_t = p2 + ' '*(25 - len(p2)) + str(qtd_carne) + ' Kg'
    p3_t = p3 + ' '*(25 - len(p3)) + 'R$ ' + str(round(preco_total, 2))
    p4_t = p4 + ' '*(25 - len(p4)) + tipo_pag
    p5_t = p5 + ' '*(25 - len(p5)) + 'R$ ' + str(round(desconto_cartao, 2))
    p6_t = p6 + ' '*(25 - len(p6)) + 'R$ ' + str(round(preco_final, 2))
    

    return f'{traco}\n{p1_t}\n{p2_t}\n{p3_t}\n{p4_t}\n{p5_t}\n{traco}\n{p6_t}\n{traco}'


def total_a_pagar(tipo_de_carne, qtd_carne, forma_pag):
    preco, tipo = calcular_preco(tipo_de_carne, qtd_carne)
    desconto_cartao = 0
    preco_total = preco * qtd_carne
    if forma_pag == 1:
        desconto_cartao = (5/100) * preco_total
        preco_final = preco_total - desconto_cartao

    else:
        preco_final = preco_total
    
    return preco_final, preco_total, desconto_cartao, tipo


def calcular_preco(tipo_de_carne, qtd_carne):
    if tipo_de_carne == 'F':
        tipo = 'File'
        preco = 5.8
        preco_final = desconto_carne(qtd_carne, preco)

    elif tipo_de_carne == 'A':
        tipo = 'Alcatra'
        preco = 6.8
        preco_final = desconto_carne(qtd_carne, preco)

    elif tipo_de_carne == 'P':
        tipo = 'Picanha'
        preco = 7.8
        preco_final = desconto_carne(qtd_carne, preco)

    return preco_final, tipo


def desconto_carne(qtd_carne, preco):
    desconto = 0
    if qtd_carne <= 5:
        desconto = 0.9
        preco_final = preco - desconto

    elif qtd_carne > 5:
        preco_final = preco - desconto

    
    return preco_final


main()