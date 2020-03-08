meses = int(input('Digite um valor em meses: '))

ano = meses // 12
resto_meses = meses % 12

print('{} meses é o equivalente á {} anos e {} meses'.format(meses, ano, resto_meses))