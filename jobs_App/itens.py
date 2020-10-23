import arquivos
from collections import namedtuple


def get_itens(dados):
    chaves = namedtuple('Chaves', list(dados[0].keys()))
    lista = []
    for dado in range(len(dados)):
        item = chaves(*list(dados[dado].values()))

        lista.append(item)

    return lista
    

def adicionar_itens(nome, marca, tela, valor, cam_frontal, dados):
    if cam_frontal != 'SIM' or cam_frontal != 'NÃO':
        if cam_frontal[0] == 'S':
            cam_frontal = 'SIM'
        else:
            cam_frontal = 'NÃO'

    novo_item = {
        'nome': nome,
        'marca': marca,
        'tela': tela,
        'valor': valor,
        'cam_frontal': cam_frontal
    }

    dados.append(novo_item)