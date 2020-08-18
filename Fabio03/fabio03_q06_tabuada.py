def main():
    tabuada()

def tabuada():
    cont = 1
    while cont <= 10:
        i = 0
        while i <= 10:
            resultado = cont * i
            print(f'{cont} X {i} = {resultado}')
            i += 1
        print('')
        cont += 1


main()