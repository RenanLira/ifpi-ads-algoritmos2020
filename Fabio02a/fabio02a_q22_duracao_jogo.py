def main():
    print('Digite o horario de inicio do jogo: ')
    hr_inicio = int(input('Hora: '))
    min_inicio = int(input('Minuto: '))
    print('Digite o horario de termino do jogo:')
    hr_termino = int(input('Hora: '))
    min_termino = int(input('Minuto: '))

    total_hr, total_min = tempo_total(hr_inicio, min_inicio, hr_termino, min_termino)

    print(f'A duração da partida foi de: {total_hr} horas e {total_min} minutos')


def tempo_total(hr_inicio, min_inicio, hr_termino, min_termino):
    total_hr = quantidade_hrs(hr_inicio, hr_termino)
    total_min = quantidade_min(min_inicio, min_termino)

    if min_inicio <= min_termino:
        return total_hr, total_min

    elif min_inicio > min_termino:
        return (total_hr - 1), total_min


def quantidade_hrs(hr_inicio, hr_termino):
    if hr_inicio >= hr_termino:
        contador = 0
        for i in range(25):
            if i > hr_inicio:
                contador +=1
            if i < hr_termino:
                contador +=1

    elif hr_inicio < hr_termino:
        contador = hr_termino - hr_inicio

    return contador


def quantidade_min(min_inicio, min_termino):
    if min_inicio <= min_termino:
        return min_termino - min_inicio

    elif min_termino < min_inicio:
        resto_min = 60 - min_inicio
        return min_termino + resto_min


main()