def main():
    num = float(input('Digite um numero "quebrado": '))

    num_arredondado = arredondar(num)

    print(f'Este numero arredondado fica: {num_arredondado}')


def arredondar(num):
    num_inteiro = int(num)

    if num - num_inteiro >= 0.5:
        return num_inteiro + 1

    elif num - num_inteiro < 0.5:
        return num_inteiro


main()