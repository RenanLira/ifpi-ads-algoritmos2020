def main():
    tabela = []
    linha = []
    for i in range(4):
        linha = list(map(int, input('linha: ').split(' ')))


        tabela.append(linha)


    
    mostrar_dados(tabela)



def mostrar_dados(tabela):
    for linha in tabela:
        for item in linha:
            print(item, end=' ')
        print('')



main()