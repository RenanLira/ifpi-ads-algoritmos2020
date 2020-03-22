def main():
    print('Tipo de combustivel: ')
    print('A - Alcool (R$ 1.90)\nG - Gasolina (R$ 2.50)')
    tipo = input('-> ').upper()
    total_litros = int(input('Litros vendidos: '))
    print('-'*30)
    print(f'preço com desconto: R$ {calcular_preco(tipo, total_litros)}')
    print(f'Preço total: R$ {total_a_pagar(tipo, total_litros):.2f}')

def total_a_pagar(tipo, total_litros):
    preco = calcular_preco(tipo, total_litros)

    return preco * total_litros

def calcular_preco(tipo, total_litros):
    preco = 0
    desconto = 0

    if tipo == 'A':
        preco = 1.90
        if total_litros <= 20:
            desconto = 3
        elif total_litros > 20:
            desconto = 5

    elif tipo == 'G':
        preco = 2.50
        if total_litros <= 20:
            desconto = 4
        elif total_litros > 20:
            desconto = 6

    preco_com_des = preco - ((desconto/100) * preco)
    
    return preco_com_des


main()
