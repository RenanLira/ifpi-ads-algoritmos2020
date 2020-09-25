def main():
    tam_vetor = int(input('Tamanho do vetor: '))

    vetor = criar_vetor(tam_vetor, -1)

    for i in range(tam_vetor):
        num = int(input('Numero: '))
        vetor[i] = num


    input(mostra_infos(vetor)+'<enter> para continuar')

    novo_vetor = substituir_numeros(vetor, 2, 2)

    print('substituindo os numeros do vetor...')
    print(novo_vetor)
    input(mostra_infos(novo_vetor)+'<enter> para continuar')

    media = tirar_media(novo_vetor)

    print(f'A media do novo vetor é: {media:.2f}')


def tirar_media(vetor):
    total = len(vetor)
    soma = 0
    for i in vetor:
        soma += i

    return soma / total
    

def substituir_numeros(vetor, num_positivo, num_negativo):
    for i in range(len(vetor)):
        if vetor[i] > 0:
            vetor[i] = vetor[i] * num_positivo

        elif vetor[i] < 0:
            vetor[i] = vetor[i] // num_negativo

    return vetor


def mostra_infos(vetor):
    pares = [0, 'pares']
    impares = [0, 'impares']
    negativos = [0, 'negativos']
    positivos = [0, 'positivos']
    for i in vetor:
        if i % 2 == 0:
            pares[0] += 1
        else:
            impares[0] += 1

        if i < 0:
            negativos[0] += 1
        elif i > 0:
            positivos[0] += 1
    

    return '-'*22+'\n' \
        +f'{pares[1]}'+espacos(20, pares[1])+f' {pares[0]}\n' \
        +f'{impares[1]}'+espacos(20, impares[1])+f' {impares[0]}\n' \
        +f'{negativos[1]}'+espacos(20, negativos[1])+f' {negativos[0]}\n' \
        +f'{positivos[1]}'+espacos(20, positivos[1])+f' {positivos[0]}\n' \
        +'-'*22+'\n'


def espacos(num, txt):
    t = num-len(txt)
    e = '-'*t

    return e


def criar_vetor(tam, valor_padrao):
    vetor = [valor_padrao] * tam
    return vetor


main()
