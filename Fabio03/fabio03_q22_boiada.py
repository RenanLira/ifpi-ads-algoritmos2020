def main():
    n = int(input('Numero de bois: '))

    cont = 1
    magro = 0
    gordo = 0
    while cont <= n:
        print(f'Ficha {cont}:')
        num_indentificacao = int(input('Numero de identificação: '))
        nome = input('Nome: ')
        peso = float(input('Peso: '))


        if peso < magro:
            magro = peso
            num_magro = num_indentificacao
            nome_magro = nome

        if peso > gordo:
            gordo = peso
            magro = gordo
            num_gordo = num_indentificacao
            nome_gordo = nome

        cont += 1

    print(f'\nBoi mais magro({nome_magro}):\nNumero de identificação: {num_magro}\nPeso: {magro}\n')
    print(f'Boi mais gordo({nome_gordo}):\nNumero de identificação: {num_gordo}\nPeso: {gordo}')


main()