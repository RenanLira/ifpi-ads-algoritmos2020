def main():
    senha = input('Senha: ')

    if validar_senha(senha):
        print('Senha correta')

    else:
        print('Senha invalida')

        
def validar_senha(senha):
    senha_correta = '1234'
    if senha == senha_correta:
        return True

    else:
        return False


main()