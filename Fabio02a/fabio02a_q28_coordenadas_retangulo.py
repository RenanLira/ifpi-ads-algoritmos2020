def main():
    print('Digite as coordenadas do primeiro ponto: ')
    x1 = int(input('x: '))
    y1 = int(input('y: '))
    print('Digite as coordenadas do segundo ponto: ')
    x2 = int(input('x: '))
    y2 = int(input('y: '))

    area = area_retangulo(x1, x2, y1, y2)

    print(f'A area do retangulo é: {area}')


def area_retangulo(x1, x2, y1, y2):
    altura = altura_retangulo(y1, y2)
    base = base_retangulo(x1, x2)

    return base * altura


def altura_retangulo(y1, y2):
    if y1 > y2:
        return y1 - y2

    else:
        return y2 - y1


def base_retangulo(x1, x2):
    if x1 > x2:
        return x1 - x2

    else:
        return x2 - x1
    

main()