def main():
    nome1 = input('Digite o nome do professor: ')
    hrs1 = int(input('Quantidade de horas dada: '))
    valor1 = float(input('Quantidade recebida por hora: '))
    print('------------------------------')
    nome2 = input('Digite o nome do segundo professor: ')
    hrs2 = int(input('Quantidade de horas dada: '))
    valor2 = float(input('Quantidade recebida por hora: '))

    resultado = comparar_prof(hrs1, hrs2, valor1, valor2)

    if resultado == 1:
        print(f'Professor(a) {nome1} tem o maior salario')

    elif resultado == 0:
        print(f'Professor(a) {nome2} tem o maior salario')

    elif resultado == 2:
        print(f'Os professores ganham o mesmo salario')
    
def comparar_prof(hrs1, hrs2, valor1, valor2):

    total_prof1 = salario_total(hrs1, valor1)
    total_prof2 = salario_total(hrs2, valor2)

    if total_prof1 > total_prof2:
        return 1

    elif total_prof1 < total_prof2:
        return 0
    
    else:
        return 2

def salario_total(hrs, valor_hrs):
    return hrs * valor_hrs


main()