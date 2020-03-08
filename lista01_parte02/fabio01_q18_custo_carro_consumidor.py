custo_fabrica = float(input('Digite o custo de fabrica do carro: '))

distribuidor = custo_fabrica * (28/100)
impostos = custo_fabrica * (45/100)
custo_total = custo_fabrica + distribuidor + impostos

print('O custo ao consumidor é de: R$ {}'.format(custo_total))