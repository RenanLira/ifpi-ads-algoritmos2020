def main():
    limite_inferior = int(input('Informe o numero de começo: '))
    limite_superior = int(input('Informe o numero de termino: '))

    verificar_primos(limite_inferior, limite_superior)


def verificar_primos(li, ls):
    while li < ls:
        if eh_primo(li):
            print(li)
        li += 1


def eh_primo(n):
    tdiv = 0
    cont = 1
    while cont <= n:
        if n % cont == 0:
            tdiv += 1
        
        cont += 1
        
    if tdiv == 2:
        return True  

    else:
        return False

main()