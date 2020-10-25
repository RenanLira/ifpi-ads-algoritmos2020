import arquivos
import itens
import time
import os
import sys


def main():
    limpar_tela()
    nome = 'celulares.bd'
    dados = arquivos.abrir_arquivo(nome)

    while True:
        limpar_tela()
        escolha = opcao()

        if escolha == 1:
            limpar_tela()
            novo_celular(dados)
        
        elif escolha == 2:
            listar(dados, 'nome', 'marca', 'valor')
            input('\n<enter> para continuar')

        elif escolha == 3:
            limpar_tela()
            buscar(dados)

        elif escolha == 0:
            arquivos.salvar_arquivo(nome, dados)
            sys.exit()


def buscar(dados):
    print(menu('Buscar Celulares'))
    print('Deixe em branco se desejar cancelar\n')

    pesquisa = control('Nome ou marca')
    tipo = control('Pesquiar por: (nome/marca)')


    if pesquisa and tipo:
        lista_nomes = dados.copy()
    
        resultado = get_resultado_pesquisa(pesquisa, tipo, lista_nomes)
        if resultado:
            selecionar(resultado, dados)
        else:
            print('nenhum resultado foi encontrado')
            input('<enter> para continuar')
    else:
        pass


def selecionar(resultado, dados):
    while True:
        listar(resultado, 'nome', 'marca', 'valor')
        print('Deixe em branco para cancelar')
        op = control('Selecione um celular', int)
        celular_selecionado = []

        if not str(op).isnumeric():
            break

        if op > len(resultado)-1 and op < 0:
            print('Digite um numero correto!')
        else:
            limpar_tela()
            celular_selecionado.append(resultado[op])
            listar(celular_selecionado, 'nome', 'marca', 'valor')
            print('1. mostrar detalhes 2.remover 3. editar 4. duplicar registro')
            op = control('>>> ', int)

            if op == 1:
                listar(celular_selecionado, 'nome', 'marca', 'valor', 'cam_frontal', 'tela')
                input('<enter> para continuar')
            
            elif op == 2:
                if input('Tem certeza que desejar apagar este item (deixe EM BRANCO para CANCELAR)\n>>>'):
                    del dados[dados.index(celular_selecionado[0])]
                    break
                else:
                    pass
            
            elif op == 3:
                editar(celular_selecionado, dados)


def editar(celular, dados):
    pass


def get_resultado_pesquisa(pesquisa, tipo, lista):

    resultado_pesquisa = sorted(lista, key= lambda a: a[tipo].find(pesquisa.upper()), reverse=True)

    for i in range(len(resultado_pesquisa), 0, -1):
        if resultado_pesquisa[i-1][tipo].find(pesquisa.upper()) == -1:
            del resultado_pesquisa[i-1]

    return resultado_pesquisa


def listar(dados, *listagem):
    print(menu('CELULARES'))
    for i in dados:
        for j in range(len(listagem)):
            print(f'{listagem[j]}: {i[listagem[j]]}')
        
        print('-'*30)

    

def novo_celular(dados):
    print(menu('Criar novo celular'))
    print('Deixe o campo em branco se desejar cancelar\n')
    lista_dados = []
    cont = 0
    for i in dados[0].keys():
        lista_dados.append(control(i, float if type(dados[0][i]) == float else str))
        if lista_dados[cont]:
            pass
        else:
            break

        cont += 1
           
    itens.adicionar_itens(*lista_dados, dados) if len(lista_dados) == len(dados[0]) else ''


def control(dado, tipo_dado=str):
    while True:
        try:
            desc_dado = input(f'{dado}: ')
            if desc_dado != '':
                return tipo_dado(desc_dado)           
            else:
                break
        except:
            print('por favor digite um valor correto')



def opcao():
    while True:
        op = input(menu('App Jobs cell','Novo celular', 'Listar celulares', 'Buscar celulares') + '\n0. Sair\n>>> ')
        if op.isnumeric():   
            return int(op)
        
        else:
            limpar_tela()
            print('Digite um numero por favor')
            time.sleep(1)
            limpar_tela()


def menu(titulo, *args):
    texto = titulo.center(30, '-') + '\n'
    contador = 1
    for i in args:
        texto += f'{contador}. {i}\n'
        contador += 1
    
    return texto



def limpar_tela():
    try:
        os.system('cls')
    except:
        os.system('clear')


if __name__ == '__main__':
    main()