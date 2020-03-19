def main():
    print('Escreva os dados na equação:')
    a = float(input('A: '))
    b = float(input('B: '))
    c = float(input('C: '))

    x1, x2 = resultado(a, b, c)
    if x1 == 0:
        print('Não há raizes')
    else:
        print(f'x1: {x1:.2f}\nx2: {x2:.2f}')


def resultado(a, b, c):
    delta = calcular_delta(a, b, c)
    if delta > 0:
        x1 = calcular_x1(a, b, c, delta)
        x2 = calcular_x2(a, b, c, delta)
        return x1, x2

    elif delta == 0:
        x = calcular_x1(a, b, c, delta)
        return x, x
    
    else:
        return 0, 0


def calcular_x1(a, b, c, delta):
    return ((-b) + (delta ** (1/2))) / (2 * a)


def calcular_x2(a, b, c, delta):
    return ((-b) - (delta ** (1/2))) / (2 * a)


def calcular_delta(a, b, c):
    return (b ** 2) - 4*a*c


main()