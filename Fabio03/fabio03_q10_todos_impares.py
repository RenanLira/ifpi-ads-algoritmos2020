def main():
    limite_inferior = int(input('Informe o numero de começo: '))
    limite_superior = int(input('Informe o numero de termino: '))

    pares(limite_superior, limite_inferior)

def pares(ls, li):
    while li <= ls:
        
        if li % 2 != 0:
            print(li)

        li += 1

main()