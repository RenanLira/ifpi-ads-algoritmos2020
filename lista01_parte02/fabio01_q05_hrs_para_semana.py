horas = int(input('Digite um valor em horas: '))

semanas = horas // 168
dias = (horas % 168) // 24
resto_horas = (horas % 168) % 24

print('{} horas é o equivalente á {} semanas {} dias e {} horas'.format(horas, semanas, dias, resto_horas))