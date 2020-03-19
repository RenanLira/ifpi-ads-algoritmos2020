def main():
    print('Digite a primeira data')
    dia1 = int(input('Dia: '))
    mes1 = int(input('Mes: '))
    ano1 = int(input('ano: '))
    print('Digite a segunda data')
    dia2 = int(input('Dia: '))
    mes2 = int(input('Mes: '))
    ano2 = int(input('ano: '))

    resultado = verificar_data(dia1, mes1, ano1, dia2, mes2, ano2)

    if resultado == 1:
        print('A primeira data é a mais recente')
    
    elif resultado == 2:
        print('A segunda data é a mais recente')

    else:
        print('As datas são iguais')


def verificar_data(dia1, mes1, ano1, dia2, mes2, ano2):
    if ano1 > ano2:
        return 1
    if ano2 > ano1:
        return 2

    else:
        if mes1 > mes2:
            return 1
        elif mes2 > mes1:
            return 2

        else:
            if dia1 > dia2:
                return 1
            elif dia2 > dia1:
                return 2
            
            else:
                return 0    


main()