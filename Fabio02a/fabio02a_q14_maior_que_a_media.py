def main():
    num1 = int(input('Digite um numero: '))
    num2 = int(input('Digite outro numero: '))
    num3 = int(input('Digite outro numero: '))
    num4 = int(input('Digite outro numero: '))
    num5 = int(input('Digite outro numero: '))

    media = calcular_media(num1, num2, num3, num4, num5)
    maiores_num = maior(num1, num2, num3, num4, num5, media)

    print(f'Os maiores valores acima da media {media} é {maiores_num}')


def calcular_media(n1, n2, n3, n4, n5):
    media = (n1 + n2 + n3 + n4 + n5) / 5

    return media

def maior(n1, n2, n3, n4, n5, media):
    maiores = []
    for i in n1, n2, n3, n4, n5:
        if i > media:
            maiores.append(i)

    return maiores


main()