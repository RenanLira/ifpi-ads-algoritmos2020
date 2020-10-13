from functools import reduce

def main():
    tamanho_matriz = int(input('Digite o tamanho da matriz quadrada: '))

    matriz = gerar_matriz(tamanho_matriz)

    print(f'Linha com a maior soma dos elementos: {maior_linha(matriz)}')
    print(f'Linha com a menor soma dos elementos: {menor_linha(matriz)}')


def gerar_matriz(tam):
    i = 1
    matriz = []
    while i <= tam:
        linha = list(map(int, input(f'Linha {i}: ').split(' ')))

        if len(linha) != tam:
            print(f'Digite {tam} numeros por favor')
        else:
            matriz.append(linha)
            i += 1

    return matriz


def maior_linha(matriz):
    maior = 0
    anterior = 0
    posicao = 0
    for i in range(len(matriz)):
        maior = reduce(lambda a, b: a+b, matriz[i])
        if maior > anterior:
            anterior = maior
            posicao = i+1
    
    return posicao


def menor_linha(matriz):
    tam_row = 0
    lista_tam = []
    for i in range(len(matriz)):
        tam_row = reduce(lambda a, b: a+b, matriz[i])
        lista_tam.append(tam_row)

    menor_tam = reduce(lambda a, b: a if a < b else b, lista_tam)
    posicao = lista_tam.index(menor_tam)+1

    return posicao


main()
