def main():
    menu = '*** Brincando com Listas ***'
    menu += '\n 1 - Inserir Valores'
    menu += '\n 2 - Mostrar Valor posição'
    menu += '\n 3 - Mostrar lista completa'
    menu += '\n 4 - Remover do Final'
    menu += '\n 5 - Remover do Início'
    menu += '\n 6 - Remover de Posição Específica'
    menu += '\n 7 - Quantidade de numeros pares'
    menu += '\n 8 - Quantidade de numeros impares'
    menu += '\n 9 - Quantidade de numeros Primos'
    menu += '\n 0 - Sair '
    menu += '\n\n Opção >>> '

    lista = []

    while True:
        opcao = int(input(menu))
        if opcao == 1:
            qtd = int(input('Digite a quantidade de numeros que deseja adicionar: '))
            inserir_valores(lista,qtd)

        elif opcao == 0:
            break

        elif len(lista) == 0:
            mostrar_msg('Insira valores na lista antes de continuar', 2)
        
        elif len(lista) != 0:
            if opcao == 2 or opcao == 6:
                posicao = int(input(f'Qual posição(0 - {len(lista)-1}) ? '))

                if posicao > len(lista)-1 or posicao < 0:
                    mostrar_msg('Valor invalido', 2)

                else:
                    if opcao == 2:
                        buscar_posicao(lista, posicao)

                    elif opcao == 6:
                        remover(lista, lista[posicao])

            elif opcao == 3:
                mostrar_lista(lista)

            elif opcao == 4:
                remover(lista, lista[len(lista)-1])

            elif opcao == 5:
                remover(lista, lista[0])

            elif opcao == 7:
                total_numeros(lista, 'par')

            elif opcao == 8:
                total_numeros(lista, 'impar')

            elif opcao == 9:
                numeros_primos(lista)


def total_numeros(lista, tipo):
    pares = 0
    impares = 0
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            pares += 1
            if tipo == 'par':
                print(f'{i} = {lista[i]}')

        elif lista[i] % 2 != 0:
            impares += 1
            if tipo == 'impar':
                print(f'{i} = {lista[i]}')
    

    if tipo == 'par':
        mostrar_msg(f'Há um total de {pares} numeros pares')

    elif tipo == 'impar':
        mostrar_msg(f'Há um total de {impares} numeros impares')


def numeros_primos(lista):
    total_primos = 0
    for i in range(len(lista)):
        contador = 0
        for j in range(1, lista[i]+1):
            if lista[i] % j == 0:
                contador += 1

        if contador == 2:
            total_primos += 1
            print(f'{i} = {lista[i]}')

    mostrar_msg(f'Há um total de {total_primos} numeros primos')



def remover(lista, num):
    continuar = input('Deseja continuar com a exclusão? (S/N): ').upper()

    if continuar == 'S':
        lista.remove(num)
        mostrar_msg('Item excluido com sucesso...')

    elif continuar == 'N':
        mostrar_msg('', 2)
    
    else:
        mostrar_msg('Opção Invalida', 2)


def mostrar_lista(lista):
    msg = ''
    for i in range(len(lista)):
        msg += f'\n{i} = {lista[i]}'

    mostrar_msg(msg, 2)


def buscar_posicao(lista, posicao):
    for i in range(len(lista)):
        if posicao == i:
            mostrar_msg(f'O valor buscado é {lista[i]}')


def inserir_valores(lista, qtd):
    for i in range(qtd):
        num = int(input(f'Valor {i+1}: '))
        lista.append(num)


    mostrar_msg('Valores adicionados com sucesso...')


def mostrar_msg(msg, tipo=1):
    print(msg)

    if tipo == 1:
        final = 'continuar'
    else:
        final = 'voltar'

    input(f'<enter> para {final}')


if __name__ == '__main__':
    main()