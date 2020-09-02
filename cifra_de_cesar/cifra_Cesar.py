def main():
    frase_inicial = input('Frase: ')
    num_rotacao = int(input('Rotação: '))

    frase_final = codificar(frase_inicial, num_rotacao)
    print(f'Frase Codificada: {frase_final}')


def codificar(frase_inicial, num_rotacao):
    nova_frase = ''
    for letra in frase_inicial:
        nova_letra = rotacao(ord(letra), num_rotacao)
        nova_frase += nova_letra

    return nova_frase
    


def rotacao(num, num_rotacao):
    #Letras maiuscula
    if num >= 65 and num <= 90:
        letra = num+num_rotacao
        if letra > 90:
            letra = letra - 26
        
        elif letra < 65:
            letra = letra + 26

        return chr(letra)

    #Letras minuscula
    if num >= 97 and num <= 122:
        letra = num+num_rotacao
        if letra > 122:
            letra = letra - 26

        elif letra < 97:
            letra = letra + 26
        
        return chr(letra)

main()