def main():
    num = int(input('Digite um numero para calcular seu fatorial: '))

    print(f'o fatorial de {num} é {calcular_fatorial(num)}')

def calcular_fatorial(num):
    resultado = 1 
    cont = 1
    while cont <= num:
        resultado *= cont
        cont += 1

    return resultado


main()