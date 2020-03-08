def main():
    nome = input('Digite algum nome: ')
    right_justify(nome)

def right_justify(s):
    espacos = 70 - len(s)
    print(' '*espacos, s)

main()