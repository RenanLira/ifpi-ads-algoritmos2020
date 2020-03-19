def main():
    data_atual = input('Digite a data atual(dd/mm/aaaa): ')
    data_aniv = input('Digite a data do seu aniversario(dd/mm/aaaa): ')

    sua_idade = calcular_idade(data_atual, data_aniv)
    print('Voce tem {} anos'.format(sua_idade))

def calcular_idade(data_atual, data_aniv):
    dia_atual, mes_atual, ano_atual = dividir_data(data_atual)
    dia_aniv, mes_aniv, ano_aniv = dividir_data(data_aniv)

    idade_anos = ano_atual - ano_aniv

    if mes_aniv >= mes_atual and dia_aniv >= dia_atual:
        return idade_anos

    return idade_anos - 1


def dividir_data(data):
    lista_data = data.split('/')

    dia = int(''.join(lista_data[0]))
    mes = int(''.join(lista_data[1]))
    ano = int(''.join(lista_data[2]))

    return dia, mes, ano

main()