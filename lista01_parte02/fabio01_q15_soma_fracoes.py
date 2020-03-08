numerador1 = int(input('Digite o numerador da primeira fração: '))
denominador1 = int(input('Digite o denominador da primeira fração: '))
numerador2 = int(input('Digite o numerador da segunda fração: '))
denominador2 = int(input('Digite o denominador da segunda fração: '))

resultado_numerador = (denominador2 * numerador1) + (denominador1 * numerador2)
resultado_denominador = denominador1 * denominador2

print('A soma das frações {}/{} + {}/{} = {}/{}'.format(numerador1, denominador1, numerador2, denominador2, resultado_numerador, resultado_denominador))