def main():
    num = int(input('Digite um numero: '))

    listar_numeros(num)

def listar_numeros(num):
    for i in range(num+1):
        if i % 2 == 0:
            print(i)

main()