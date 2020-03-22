def main():
    valor_hr = float(input('Valor da sua hora de trabalho: R$ '))
    tempo_hrs = int(input('Horas trabalhadas: '))
    
    salario, salario_liquido, ir, desconto_ir, total_descontos = calcular_salario(valor_hr, tempo_hrs)

    print('-'*30)
    print(f'Salario Bruto ({valor_hr} * {tempo_hrs}): R$ {salario:.2f}')
    print(f'(-) IR({desconto_ir}%): R$ {ir:.2f}')
    print(f'(-) INSS(10%): R$ {inss(salario):.2f}')
    print(f'FGTS(11%): R$ {fgts(salario):.2f}')
    print(f'Total Descontos: R$ {total_descontos:.2f}')
    print(f'Salario liquido: R$ {salario_liquido:.2f}')
    print('-'*30)


def calcular_salario(valor_hr, tempo_hrs):
    salario = valor_hr * tempo_hrs
    desconto_ir = imposto_renda(salario)

    ir = (desconto_ir/100) * salario
    total_inss = inss(salario)
    total_descontos = total_inss + ir

    salario_liquido = salario - total_descontos

    return salario, salario_liquido, ir, desconto_ir, total_descontos


def fgts(salario):
    return (11/100) * salario


def inss(salario):
    return(10/100) * salario


def imposto_renda(salario):
    if salario > 0 and salario <= 900:
        return 0

    elif salario > 900 and salario <= 1500:
        return 5

    elif salario > 1500 and salario <= 2500:
        return 10

    elif salario > 2500:
        return 20


main()