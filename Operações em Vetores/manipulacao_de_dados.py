def main():
    menu = '*** Brincando com Listas ***'
    menu += '\n 1 - Inserir Valores'
    menu += '\n 2 - Mostrar Valor posição'
    menu += '\n 3 - Mostrar lista completa'
    menu += '\n 4 - Remover do Final'
    menu += '\n 5 - Remover do Início'
    menu += '\n 6 - Remover de Posição Específica'
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

                if posicao > qtd or posicao < 0:
                    mostrar_msg('Valor invalido', 2)

                else:
                    if opcao == 2:
                        buscar_posicao(lista, posicao)

                    elif opcao == 6:
                        continuar = input('Deseja continuar com a exclusão? (S/N): ').upper()
                        if continuar == 'S':
                            remover(lista, lista[posicao])
                        elif continuar == 'N':
                            mostrar_msg('', 2)
                        else:
                            mostrar_msg('Opção invalida...', 2)
            
            
            elif opcao == 3:
                mostrar_lista(lista)

            elif opcao == 4 or opcao == 5:
                continuar = input('Deseja continuar com a exclusão? (S/N): ').upper()

                if continuar == 'S':
                    if opcao == 4:
                        remover(lista, lista[len(lista)-1])
                    elif opcao == 5:
                        remover(lista, lista[0])

                elif continuar == 'N':
                    mostrar_msg('', 2)
                else:
                    mostrar_msg('Opção invalida...', 2)
            
                

def remover(lista, num):
    lista.remove(num)
    mostrar_msg('Item excluido com sucesso...')


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
        num = float(input(f'Valor {i+1}: '))
        lista.append(num)


    mostrar_msg('Valores adicionados com sucesso...')


def mostrar_msg(msg, modo=1):
    print(msg)

    if modo == 1:
        final = 'continuar'
    else:
        final = 'voltar'

    input(f'<enter> para {final}')


main()