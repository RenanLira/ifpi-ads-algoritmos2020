def main():
    n = int(input('Quantidade de habitantes: '))

    cont = 1
    total_salario = 0
    total_filhos = 0
    quant_menor = 0
    while cont <= n:
        print(f'Habitante {cont}')
        salario = float(input('Salario: '))
        num_filhos = int(input('Quantidade de filhos: '))

        total_salario = total_salario + salario
        total_filhos = total_filhos + num_filhos

        if salario <= 1000:
            quant_menor += 1

        cont+=1

    media_salario = total_salario / n
    media_filhos = total_filhos / n
    percentual_menor = (quant_menor / n) * 100

    print(f'\nMedia de salario: R$ {media_salario:.2f}')
    print(f'Media de filhos: {media_filhos:.0f}')
    print(f'Percentual de pessoas que recebem até R$ 1000: {percentual_menor:.2f}%')


main()
