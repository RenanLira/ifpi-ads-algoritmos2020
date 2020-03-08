quant_cobre = int(input('Digite a quantidade de cobre(em kg): '))
quant_zinco = int(input('Digite a quantidade de zinco(em kg): '))

latao_cobre = quant_cobre * (70/100)
latao_zinco = quant_zinco * (30/100)

qtd_latao = latao_cobre + latao_zinco
qtd_latao = int(qtd_latao)

print('A quantidade de latao possivel é de: {}'.format(qtd_latao))


