def main():
    limite_inferior = int(input('Informe o numero de começo: '))
    limite_superior = int(input('Informe o numero de termino: '))

    verificar_primos(limite_inferior, limite_superior)


def verificar_primos(li, ls):
    
    for i in range(li, ls):
        if eh_primo(i):
            print(i)


def eh_primo(n):
    tdiv = 0
    for i in range(1, n+1):
        if n % i == 0:
            tdiv += 1

    if tdiv == 2:
        return True  

    else:
        return False
    

main()