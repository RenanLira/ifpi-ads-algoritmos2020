import os
import json
import collections


def abrir_arquivo(nome):
    get_dados = []

    if os.path.exists(nome):
        arquivo = open(nome, 'r')
        dados = arquivo.readline()
        get_dados = json.loads(dados)

        arquivo.close()


    return get_dados


def salvar_arquivo(nome, dados):
    arquivo = open(nome, 'w')

    novos_dados = json.dumps(dados)
    arquivo.write(novos_dados)

    arquivo.close()


 