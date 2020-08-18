def main():
    a = int(input('Digite o valor inicial: '))
    limite = int(input('Digite o valor final: '))
    razao = int(input('Digite o valor da razão geometrica: '))

    progressao_geometrica(a, limite, razao)

def progressao_geometrica(a, limite, razao):
    while a <= limite:
        if a == 0: # evitar loop infinito caso "a" seja 0
            a = 1
        
        print(a)
        a *= razao

main()