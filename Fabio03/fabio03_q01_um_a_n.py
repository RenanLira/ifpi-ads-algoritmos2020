def main():
    num = int(input('Digite um numero: '))

    listar_numeros(num)

def listar_numeros(num):
    cont = 0
    while cont <= num:
        print(cont)

        cont += 1

main()