minutos = int(input('Digite uma quantidade em minutos: '))

dias = minutos // 1440
horas = (minutos % 1440) // 60
resto_minutos = (minutos % 1440) % 60

print('{} minutos é o equivalente a {} dias {} horas e {} minutos'.format(minutos, dias, horas, resto_minutos))