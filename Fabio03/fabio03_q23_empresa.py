def main():
    num_func = int(input('Digite a quantidade de funcionarios: '))

    cont = 1
    valor_hr = 12
    valor_depedente = 40
    inss = 8.5 / 100
    ir = 5 / 100
    while cont <= num_func:
        print(f'Ficha {cont}')
        codigo = int(input('Codigo: '))
        hrs_trabalho = int(input('Horas trabalhadas: '))
        num_dependentes = int(input('Nº de dependentes: '))

        total_hr = valor_hr * hrs_trabalho
        total_depen = valor_depedente * num_dependentes
        salario = total_hr + total_depen

        desconto_inss = inss * salario
        desconto_ir = ir * salario

        salario_liquido = salario - (desconto_inss + desconto_ir)

        print('')

        print(f'Desconto INSS: R$ {desconto_inss:.2f}')
        print(f'Desconto IR: R$ {desconto_ir:.2f}')
        print(f'Salario liquido: R$ {salario_liquido:.2f}\n')

        cont+=1


main()


