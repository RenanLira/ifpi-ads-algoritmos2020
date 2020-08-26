def main():
    n = int(input('Digite o valor de N: '))

    i = 1
    resultado = 0
    while i <= n:
        fracao = 1/i
        if i%2 != 0:
            resultado = fracao + resultado
            
        else:
            resultado = resultado - fracao

        i += 1
        
    print(f'o resultado da somatoria das frações ate {n}: {resultado:.2f}')


main()