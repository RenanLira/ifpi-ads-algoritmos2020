# fin = open('words.txt')

# for line in fin:
#     word = line.strip()

#     print(word)



def main():

    while True:
        opcao = int(input(imprimir_menu()))
        if opcao == 1:
            mais_de_20_letras()

        elif opcao == 2:
            has_no_e()

        elif opcao == 3:
            sub_menu = '1 - Que não contem tais letras\n' \
                + '2 - Que contem tais letras\n' \
                + '0 - Voltar\n' \
                + '-> '

            while True:
                sub_opcao = int(input(sub_menu))

                if sub_opcao == 1:
                    letras = input('Digite as letras proibidas(sem espaços): ')
                    avoids(letras)
                elif sub_opcao == 2:
                    letras = input('Digite as letras contidas(sem espaços): ')
                    uses_only(letras)
                elif sub_opcao == 0:
                    break
    

        elif opcao == 0:
            break


def avoids(letras):
    arquivo = open('words.txt')
    for linha in arquivo:
        cont = 0
        palavra = linha.strip()
        for letra in letras:
            if verificar_letra(palavra, letra):
                cont+=1
        
        if cont == len(letras):
            print(palavra)

    arquivo.close()


def uses_only(letras):
    arquivo = open('words.txt')
    for linha in arquivo:
        cont = 0
        palavra = linha.strip()
        for letra in letras:
            if not verificar_letra(palavra, letra):
                cont+=1
        
        if cont == len(letras):
            print(palavra)

    arquivo.close()


def mais_de_20_letras():
    arquivo = open('words.txt')

    for linha in arquivo:
        palavra = linha.strip()
        if len(palavra) > 20:
            print(palavra)

    arquivo.close()


def has_no_e():
    arquivo = open('words.txt')

    palavras_sem_e = 0
    total_palavras = 0


    for linha in arquivo:
        total_palavras += 1
        palavra = linha.strip()

        if verificar_letra(palavra, 'e'):
            palavras_sem_e += 1
            print(palavra)


    porcentagem = (palavras_sem_e / total_palavras) * 100

    print(f'Total de palavras sem "e": {palavras_sem_e}')
    print(f'Total de palavras: {total_palavras}')
    print(f'Percentual de palavras sem "e": {porcentagem:.2f}%')

    arquivo.close()


def verificar_letra(palavra, l):
    for letra in palavra:
        if letra == l:
            return False
    
    return True


def imprimir_menu():
    menu = '---------- WORDPLAY ----------\n' \
        + '1 - Palavras com mais de  20 letras\n' \
        + '2 - Vereficar palavras sem "e"\n' \
        + '3 - Buscar palavras\n' \
        + '0 - Sair\n' \
        + '-> '

    
    return menu




main()