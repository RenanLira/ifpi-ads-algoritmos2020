import functools

def main():
    lista = list(map(int, input('Digite os numeros: ').split(' ')))

    if verificar_numeros(lista):
        print('Há numeros iguais')

    else:
        print('não há numeros iguais na lista')
        



def verificar_numeros(lista):
    for i in range(len(lista)):
        # print(f'numero em verificação: {lista[i]}')
        for j in range(i+1, len(lista)):
            # print(f'outros numeros: {lista[j]}')
            if lista[i] == lista[j]:
                return True

    return False

main()