def main():
    print('Digite os dados do triangulo: ')
    a = float(input('Lado 1: '))
    b = float(input('Lado 2: '))
    c = float(input('Lado 3: '))

    hipotenusa, cateto1, cateto2 = verificar_triangulo(a, b, c)

    if verificar_triangulo(a, b, c):
        print(f'Hipotenusa: {hipotenusa}\nCatetos: {cateto1}, {cateto2}')

def verificar_triangulo(a, b, c):
    hipotenusa = descobrir_hipot(a, b, c)
    cateto1, cateto2 = descobrir_catetos(a, b, c, hipotenusa)

    if hipotenusa == cateto1 and hipotenusa == cateto2:
        return False

    else:
        return hipotenusa, cateto1, cateto2


def descobrir_catetos(a, b, c, hipotenusa):
    if a == hipotenusa:
        return b, c
    
    elif b == hipotenusa:
        return a, c
    
    elif c == hipotenusa:
        return a, b


def descobrir_hipot(a, b, c):
    hipotenusa = 0
    for i in a, b, c:
        if hipotenusa < i:
            hipotenusa = i
    
    return hipotenusa


main()