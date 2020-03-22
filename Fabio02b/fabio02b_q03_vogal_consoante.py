def main():
    letra = input('Digite uma letra: ').upper()

    print(f'Essa letra é uma {verificar_letra(letra)}')


def verificar_letra(letra):
    vogal = 0
    for i in 'A', 'E', 'I', 'O', 'U':
        if letra == i:
            vogal = 1

    if vogal == 1:
        return 'vogal'

    else:
        return 'consoante'
    

main()    