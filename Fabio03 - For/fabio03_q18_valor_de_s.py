def main():
    n = int(input('Digite o valor de N: '))

    i = 1
    q = 0
    resultado = 0
    while i <= n:
        fracao = i/(n-q)
        resultado = resultado + fracao
        i += 1
        q += 1

    print(f'o resultado da somatoria das frações ate {n}: {resultado:.2f}')
    

main()