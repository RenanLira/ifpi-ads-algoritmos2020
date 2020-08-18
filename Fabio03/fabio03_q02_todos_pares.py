def main():
    num = int(input('Digite um numero: '))

    listar_numeros(num)

def listar_numeros(num):
    cont = 1
    while cont <= num:
        if cont % 2 == 0:
            print(cont)

        cont += 1

main()