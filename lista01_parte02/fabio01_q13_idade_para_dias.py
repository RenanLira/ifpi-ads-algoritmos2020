anos = int(input('Quantos anos vc tem: '))
meses = int(input('E quantos meses: '))
dias = int(input('E quantos dias: '))

total_dias = (anos * 365) + (meses * 31) + dias

print('Vc tem o total de: {} dias'.format(total_dias))