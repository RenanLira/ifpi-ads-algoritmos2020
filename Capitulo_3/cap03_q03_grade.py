def main():
    imprimir_grade()

def imprimir_grade():
    mais_menos()
    do_four(barra)
    mais_menos()
    do_four(barra)
    mais_menos()

def mais_menos():
    print('+', end='')
    print(' -'*4, end=' ')
    print('+', end='')
    print(' -'*4, end=' ')
    print('+')

def barra():
    print('|', ' '*8, end='')
    print('|', ' '*8, end='')
    print('|')

def do_four(f):
    f()
    f()
    f()
    f()

if __name__ == "__main__":
    main()