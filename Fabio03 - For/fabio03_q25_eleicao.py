def main():
    n = int(input('Quantidade de eleitores: '))

    i = 1
    candidato1 = 0
    candidato2 = 0
    candidato3 = 0
    nulo = 0
    branco = 0
    while i <= n:
        voto = int(input('Voto: '))

        if voto > 0 and voto <= 3:
            if voto == 1:
                candidato1 += 1
                
            elif voto == 2:
                candidato2 += 1
                
            else:
                candidato3 += 1
                
        
        elif voto == 0:
            branco += 1
        
        else:
            nulo += 1

        i += 1

    if candidato1 > candidato2 and candidato1 > candidato3:
        print('Vencedor: Candidato 1')

    elif candidato2 > candidato1 and candidato2 > candidato3:
        print('Vencedor: Candidato 2')
    
    elif candidato3 > candidato2 and candidato3 > candidato2:
        print('Vencedor: Candidato 3')
    
    else:
        print('Empate')

    print(f'Total Votos: {n}\nCandidato 1: {candidato1}\nCanditado 2: {candidato2}\nCanditado 3: {candidato3}')
    print(f'Total nulos: {nulo}')
    print(f'Total em branco: {branco}')

main()