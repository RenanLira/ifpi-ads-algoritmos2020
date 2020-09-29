def main():
    i = 1
    q = 1
    resultado = 0
    while i <= 99:
        fracao = i/q

        resultado = resultado + fracao

        i += 2
        q += 1

    print(f'o resultado da somatoria das frações ate 99/50: {resultado:.2f}')


main()