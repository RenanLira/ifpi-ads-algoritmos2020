def main():
    num1 = int(input('Digite um numero: '))
    num2 = int(input('Digite outro numero: '))
    num3 = int(input('Digite outro numero: '))

    maior, meio, menor = ordem_crescente(num1, num2, num3)

    print('{}, {}, {}'.format(menor, meio, maior))

    
def ordem_crescente(num1, num2, num3):
    maior = maior_num(num1, num2, num3)
    menor = menor_num(num1, num2, num3, maior)
    meio = meio_num(num1, num2, num3, menor, maior)

    return maior, meio, menor

def maior_num(num1, num2, num3):
    maior = 0
    for i in num1, num2, num3:
        if maior < i:
            maior = i
    return maior


def menor_num(num1, num2, num3, maior):
    menor = maior
    for i in num1, num2, num3:
        if menor > i:
            menor = i
    return menor


def meio_num(num1, num2, num3, menor, maior):
    meio = 0
    for i in num1, num2, num3:
        if i > menor and i < maior:
            meio = i
    return meio


main()