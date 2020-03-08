anos_fumando = int(input('A quantos anos vc fuma? '))
cigarros_por_dia = int(input('Numero de cigarros fumados por dia: '))
preco_carteira = float(input('Preço da carteira de cigarro: '))

total_cigarros = (anos_fumando * 365) * cigarros_por_dia

total_gasto = (total_cigarros // 20) * preco_carteira

print('Total gasto em cigarros: {}'.format(total_gasto))