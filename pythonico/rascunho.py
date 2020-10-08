import os

def main():
    while condicao:
        try:
            numeros = list(map(lambda a: int(a)*2 if a else '', input('->(deixe vazio para cancelar) ').split(' ')))
            
            break
        except:
            os.system('cls')
            print('digite numeros por favor')
    
    
    print(numeros)





if __name__ == '__main__':
    main()

