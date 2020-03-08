def main():
    do_four(print_twice, 'spam')

def print_spam():
    print('spam')

def do_twice(f, v):
    f(v)
    f(v)

def print_twice(bruce):
    print(bruce)
    print(bruce)

def do_four(f, v):
    do_twice(f, v)
    do_twice(f, v)

main()