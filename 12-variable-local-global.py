print('\n-------------  Variable Globales-----------------\n')

number_int = 33

print("\n\t\t::::::: ---- :::::::\n")

def start():
    number = 5
    number_int = 25
    print(number_int)


def run():
    print(number_int)


start()
run()


print("\n\t\t::::::: ---- :::::::\n")

def start1():
    number = 5
    global number_int
    number_int = 25
    print(number_int)


def run1():
    print(number_int)

start1()
run1()

print('\n------------- Variable Locales-----------------\n')

print("\n\t\t::::::: funcion anidadas :::::::\n")


def test():
    a = 1
    #print(a)
    def anidadas():
        a = 2
        print(a)
    anidadas()
    print(a)


test()

print("\n\t\t::::::: --- :::::::\n")

def test1():
    a = 1
    
    def anidadas():
        nonlocal a    # variable  local (sub global, dentro de una funcion anidada)
        a = 7
        print(a)
    anidadas()
    print(a)

test1()








