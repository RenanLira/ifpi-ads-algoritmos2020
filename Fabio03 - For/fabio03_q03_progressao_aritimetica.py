def main():
    a = int(input('Digite o valor inicial: '))
    limite = int(input('Digite o valor final: '))
    razao = int(input('Digite o valor da razão aritimetica: '))

    progressao_aritimetica(a, limite, razao)


def progressao_aritimetica(a, limite, razao):
    for i in range(a, limite, razao):
        print(i)

main()