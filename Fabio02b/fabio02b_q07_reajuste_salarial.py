def main():
    salario = float(input('Digite o salario do funcionario: R$ '))

    if reajustar_salario(salario):
        novo_salario, porcentagem, aumento = reajustar_salario(salario)

        print('-'*30)
        print(f'Salario antigo: R$ {salario}')
        print(f'Percentual de aumento aplicado: {porcentagem}%')
        print(f'Valor do aumento: R$ {aumento}')
        print(f'Novo salario: R$ {novo_salario}')
        print('-'*30)

    else:
        print('Salario Invalido')


def reajustar_salario(salario):
    porcentagem = 0
    aumento = 0
    novo_salario = 0

    if salario > 0 and salario <= 280:
        porcentagem = 20
        aumento = calcular_porcentagem(salario, porcentagem)

    elif salario > 280 and salario <= 700:
        porcentagem = 15
        aumento = calcular_porcentagem(salario, porcentagem)

    elif salario > 700 and salario <= 1500:
        porcentagem = 10

    elif salario > 1500:
        porcentagem = 5

    else:
        return False

    aumento = calcular_porcentagem(salario, porcentagem)
    novo_salario = calcular_aumento(salario, aumento)

    return novo_salario, porcentagem, aumento


def calcular_aumento(salario, aumento):
    return salario + aumento


def calcular_porcentagem(salario, porcentagem):
    return (porcentagem / 100) * salario


main()