def main():
    matriz = []

    for i in range(4):
        row = list(map(int, input(f'Digite 4 elementos da {i+1} linha: ').split()))

        matriz.append(row)

    print(f'a somatoria da diagonal principal é: {diagonal_principal(matriz)}')
    print(f'a somatoria da diagonal secundaria é: {diagonal_secundaria(matriz)}')
    print(f'a somatoria dos outros numeros é: {fora_da_diagonal(matriz)}')


def diagonal_principal(matriz):
    somatoria = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i == j:
                somatoria += matriz[i][j]

    return somatoria


def diagonal_secundaria(matriz):
    somatoria = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if (i+1) + (j+1) == len(matriz) + 1:
                somatoria += matriz[i][j]

    return somatoria


def fora_da_diagonal(matriz):
    somatoria = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if (i+1) + (j+1) != len(matriz) + 1 and i != j:
                somatoria += matriz[i][j]

    return somatoria


main()