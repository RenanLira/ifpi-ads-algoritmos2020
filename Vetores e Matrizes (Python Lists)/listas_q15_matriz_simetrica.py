def main():
    matriz = []

    for i in range(4):
        row = list(map(int, input(f'Digite 4 elementos da {i+1} linha: ').split()))

        matriz.append(row)

    
    if eh_simetrica(matriz):
        print('Esta matriz é simetrica')
    
    else:
        print('ela não é simetrica')



def eh_simetrica(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == matriz[j][i]:
                return True

    return False

main()