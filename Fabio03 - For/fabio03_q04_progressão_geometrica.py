def main():
    a = int(input('Digite o valor inicial: '))
    limite = int(input('Digite o valor final: '))
    razao = int(input('Digite o valor da razão geometrica: '))

    progressao_geometrica(a, limite, razao)

def progressao_geometrica(a, limite, razao):
    for i in range(a, limite):
        formula = a * razao **(i - 1)
        if formula > limite:
            break
        print(formula)

main()