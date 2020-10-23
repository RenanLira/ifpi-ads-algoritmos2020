import arquivos
import itens
import time
import os
import sys


def main():
    os.system('cls')
    nome = 'celulares.bd'
    dados = arquivos.abrir_arquivo(nome)

    while True:
        os.system('cls')
        escolha = opcao()

        if escolha == 1:
            os.system('cls')
            novo_celular(dados)
        
        elif escolha == 2:
            listar(dados)

        elif escolha == 0:
            arquivos.salvar_arquivo(nome, dados)
            sys.exit()


def listar(dados):
    get_itens = itens.get_itens(dados)

    print(menu('CELULARES'))
    for item in get_itens:
        print(''.center(30, '-'))
        print(f'Nome: {item.nome}')
        print(f'Marca: {item.marca}')
        print(f'Tela: {item.tela}')
        print(f'Valor: R$ {item.valor}')
        print(f'Camera: {item.cam_frontal}')

    input('\n<enter> para continuar')
    

def novo_celular(dados):
    print(menu('Criar novo celular'))
    print('Deixe o campo em branco se desejar cancelar\n')
    while True:
        nome = input('Nome: ')
        if nome == '':
            break

        marca = input('Marca: ')
        if marca == '':
            break

        try:
            tela = float(input('Tela("): '))
            if tela == '':
                break

            valor = float(input('Valor: R$ '))
            if valor == '':
                break

            cam_frontal = input('Camera frontal (sim/nao): ').upper()
            if cam_frontal == '':
                break

        except:
            print('digite um valor correto')
        
        itens.adicionar_itens(nome, marca, tela, valor, cam_frontal, dados)
        break


def opcao():
    while True:
        op = input(menu('App Jobs cell','Novo celular', 'Listar celulares') + '\n0. Sair\n>>> ')
        if op.isnumeric():   
            return int(op)
        
        else:
            os.system('cls')
            print('Digite um numero por favor')
            time.sleep(1)
            os.system('cls')


def menu(titulo, *args):
    texto = titulo.center(30, '-') + '\n'
    contador = 1
    for i in args:
        texto += f'{contador}. {i}\n'
        contador += 1
    
    return texto


if __name__ == '__main__':
    main()