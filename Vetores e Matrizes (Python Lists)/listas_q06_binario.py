def main():
    num_binario = []
    for i in range(8):
        num = int(input(f'posição {i}: '))
        num_binario.append(num)

    print(f'Decimal: {para_decimal(num_binario)}')

    print(f'Hexadecimal: {para_hexadecimal(num_binario)}')


def para_decimal(binario):
    total = 0
    multi = 0

    for i in range(len(binario)):
        if binario[i] == 1:
            multi = binario[i] * (2**i)
            total += multi
    
    return total


def para_hexadecimal(binario):
    sub_grupo = []
    resultado = ''
    for i in range(len(binario)-1,-1, -1):
        sub_grupo.append(binario[i])

        if len(sub_grupo) == 4:
            multi = 0
            letra = ord('A') - 10

            sub_grupo.reverse()

            for j in range(len(sub_grupo)):
                multi += sub_grupo[j] * (2**j)

            if multi > 9:
                nova_letra = chr(letra+multi)
                resultado += nova_letra

            else:
                resultado += str(multi)

            sub_grupo.clear()

    return resultado



main()