def main():
    num1 = int(input('Digite um numero: '))
    num2 = int(input('Digite outro numero: '))
    num3 = int(input('Digite outro numero: '))

    resultado = maior_num(num1, num2, num3)

    print('O maior numero é: {}'.format(resultado))
def maior_num(num1, num2, num3):
    maior = 0
    for i in num1, num2, num3:
        if maior < i:
            maior = i

    return maior


main()