def main():
    tabuada()


def tabuada():

    for i in range(1, 11):
        for k in range(11):
            resultado = i * k
            print(f'{i} X {k} = {resultado}')

        print('')


main()