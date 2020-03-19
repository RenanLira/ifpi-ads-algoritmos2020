def main():
    altura = float(input('Qual a sua altura: '))
    peso = float(input('Qual o seu peso: '))

    print(f'Você está com {resultado_imc(altura, peso)} ')


def resultado_imc(altura, peso):
    imc = peso / (altura ** 2)

    if imc < 25:
        return 'peso normal'

    elif imc >= 25 and imc <= 30:
        return 'obeso'

    elif imc > 30:
        return 'obesidade mórbida'


main()