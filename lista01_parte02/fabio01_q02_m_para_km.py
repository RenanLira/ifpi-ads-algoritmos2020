metros = int(input('Digite um valor em metros: '))

km = metros // 1000
resto_metros = metros % 1000

print('O total em quilometros é: {}km e {}m'.format(km, resto_metros))