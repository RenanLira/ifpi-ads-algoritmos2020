def main():
    num = int(input('Digite um numero para calcular seu fatorial: '))

    print(f'o fatorial de {num} é {calcular_fatorial(num)}')

def calcular_fatorial(num):

    resultado = 1
    for i in range(1, num+1):
        resultado *= i
        

    return resultado


main()