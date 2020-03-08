valor_min = int(input('Digite um valor em minutos: '))

total_hrs = valor_min // 60
resto_min = valor_min % 60

print('O total em horas é {} hora(s) e {} minuto(s)'.format(total_hrs, resto_min))