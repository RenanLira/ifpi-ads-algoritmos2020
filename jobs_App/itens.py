import arquivos
from collections import namedtuple


# def get_itens(dados):
#     lista = []
#     for dado in dados:
#         lista.append(dado)

#     return lista
    

def adicionar_itens(nome, marca, tela, valor, cam_frontal, dados):
    cam_frontal = cam_frontal.upper()
    if cam_frontal != 'SIM' or cam_frontal != 'NÃO':
        if cam_frontal[0] == 'S':
            cam_frontal = 'SIM'
        else:
            cam_frontal = 'NÃO'

    novo_item = {
        'nome': nome.upper(),
        'marca': marca.upper(),
        'tela': tela,
        'valor': valor,
        'cam_frontal': cam_frontal
    }

    dados.append(novo_item)