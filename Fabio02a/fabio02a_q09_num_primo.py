def main():
    numero = int(input('Digite um numero: '))

    resultado = eh_primo(numero)

    print('O numero {} {}'.format(numero, resultado))


def eh_primo(num):
    divisores = 0
    for i in range(1, num):
        if num % i == 0:
            divisores += 1

    if divisores > 1:
        return 'não é primo'
    
    else:
        return 'é primo'

main()