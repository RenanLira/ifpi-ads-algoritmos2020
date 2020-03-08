segundos = int(input('Digite uma quantidade em segudos: '))

horas = segundos // 3600
minutos = (segundos % 3600) // 60
resto_segundos = (segundos % 3600) % 60

print('{} segundos é igual á {} horas {} minutos e {} segundos'.format(segundos, horas, minutos, resto_segundos))