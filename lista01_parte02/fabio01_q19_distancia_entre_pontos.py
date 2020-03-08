print('Digite as coordenadas do ponto 1:')
x1 = float(input('x: '))
y1 = float(input('y: '))
print('Digite as coordenadas do ponto 2:')
x2 = float(input('x: '))
y2 = float(input('y: '))

distancia = (((x2 + x1)**2) + ((y2 - y1)**2)) ** (1/2)

print('A distancia entre os pontos é de: {:.2f}'.format(distancia))