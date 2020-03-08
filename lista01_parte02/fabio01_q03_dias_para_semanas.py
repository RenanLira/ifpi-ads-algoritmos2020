dias = int(input('Digite uma quantidade em dias: '))

semanas = dias // 7
resto_dias = dias % 7

print('{} dia(s) é equivalente á {} semana(s) e {} dia(s)'.format(dias, semanas, resto_dias))