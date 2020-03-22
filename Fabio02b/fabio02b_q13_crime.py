def main():
    print('-'*30)
    print('RESPONDA AS RESPOSTAS ABAIXO (S/N)')
    print('-'*30)
    p1 = input('Telefonou para a vítima ? ').upper()
    p2 = input('Esteve no local do crime ? ').upper()
    p3 = input('Mora perto da vítima ? ').upper()
    p4 = input('Devia para a vítima ? ').upper()
    p5 = input('Já trabalhou com a vítima? ').upper()
    print('-'*30)

    total = contar_sim(p1, p2, p3, p4, p5)

    print(f'Essa pessoa está classificado como {verificar_suspeito(total)}')
    print('-'*30)

def verificar_suspeito(total_sim):
    if total_sim == 5:
        return 'Assassino'

    elif total_sim >= 3 and total_sim <= 4:
        return 'Cúmplice'

    elif total_sim == 2:
        return 'Suspeita'

    else:
        return 'Inocente'


def contar_sim(p1, p2, p3, p4, p5):
    total = 0
    for i in p1, p2, p3, p4, p5:
        if i == 'S':
            total +=1
        
    return total


main()