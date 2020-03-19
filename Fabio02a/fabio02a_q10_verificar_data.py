def main():
    data = input('Digite uma data(dd/mm/aaaa): ')
    resultado = verificar_data(data)

    print('A data {}, {}'.format(data, resultado))


def verificar_data(data):
    dia, mes, ano = dividir_data(data)
    if verificar_mes(mes) and verificar_dia(dia, mes, ano):
        return 'é valida'
    else:
        return 'não é valida'
    

def eh_bisexto(ano):
    if ano % 4 == 0:
        if ano % 100 != 0:
            return True
        else: 
            return False

    elif ano % 400 == 0:
        return True
    
    else: 
        return False


def verificar_mes(mes):
    if mes > 12 or mes < 1:
        return False

    else:
        return True


def verificar_dia(dia, mes, ano):
    if mes == 2:
        if eh_bisexto(ano):
            if dia <= 29:
                return True
            else:
                return False

        else:
            if dia <= 28:
                return True
            else:
                return False
                
    if mes <= 7:
        if mes % 2 == 0:
            if dia <= 30:
                return True
            else:
                return False

        if mes % 2 != 0:
            if dia <= 31:
                return True
            else:
                return False

    else:
        if mes % 2 == 0:
            if dia <= 31:
                return True
            else:
                return False

        if mes % 2 != 0:
            if dia <= 30:
                return True
            else:
                return False


def dividir_data(data):
    lista_data = data.split('/')

    dia = int(''.join(lista_data[0]))
    mes = int(''.join(lista_data[1]))
    ano = int(''.join(lista_data[2]))

    return dia, mes, ano


main()