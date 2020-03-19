def main():
    print('Digite a data que voce nasceu: ')
    dia_ani = int(input('Dia: '))
    mes_ani = int(input('Mes: '))
    ano_ani = int(input('Ano: '))
    print('Digite a data de hoje: ')
    dia_atual = int(input('Dia: '))
    mes_atual = int(input('Mes: '))
    ano_atual = int(input('Ano: '))

    ano, mes, dia = calcular_idade(dia_ani, mes_ani, ano_ani, dia_atual, mes_atual, ano_atual)

    print(f'Voce tem {ano} anos {mes} meses e {dia} dias')


def calcular_idade(dia_ani, mes_ani, ano_ani, dia_atual, mes_atual, ano_atual):
    total_dias_ani = transformar_em_dias(dia_ani, mes_ani, ano_ani)
    total_dias_atual = transformar_em_dias(dia_atual, mes_atual, ano_atual)

    diferenca = total_dias_atual - total_dias_ani

    total_ano = diferenca // 365
    total_mes = int((diferenca % 365) // 30.5)
    total_dia = int((diferenca % 365) % 30.5)

    return total_ano, total_mes, total_dia


def transformar_em_dias(dia, mes, ano):
    ano_em_dias = int(ano * 365)
    meses_em_dias = int(mes * 30.5)
    resto_dias = dia

    total_dias = ano_em_dias + meses_em_dias + resto_dias

    return total_dias
    



main()