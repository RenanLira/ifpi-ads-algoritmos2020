def main():
    num1 = int(input('Digite um numero: '))
    num2 = int(input('Digite outro numero: '))
    num3 = int(input('Digite outro numero: '))
    num4 = int(input('Digite outro numero: '))
    num5 = int(input('Digite outro numero: '))

    maior_num = maior_numero(num1, num2, num3, num4, num5)
    menor_num = menor_numero(num1, num2, num3, num4, num5, maior_num)

    print(f'O maior numero é: {maior_num}')
    print(f'O menor numero é: {menor_num}')


def maior_numero(n1, n2, n3, n4, n5):
    maior = 0
    for i in n1, n2, n3, n4, n5:
        if maior < i:
            maior = i

    return maior


def menor_numero(n1, n2, n3, n4, n5, maior):
    menor = maior
    for i in n1, n2, n3, n4, n5: 
        if menor > i:
            menor = i

    return menor


main()