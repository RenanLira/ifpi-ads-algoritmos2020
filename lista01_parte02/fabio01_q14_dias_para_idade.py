idade_dias = int(input('Qual a sua idade em dias: '))

anos = idade_dias // 365
meses = (idade_dias % 365) // 31
dias =  (idade_dias % 365) % 31

print('Vc tem {} anos {} meses e {} dias'.format(anos, meses, dias))