print('\n------------- FUNCIONES - Expresion Lambda-----------------\n')
print("\n::::::: funcion normal :::::::\n")

def sumas(a, b):
    return a + b

valor = sumas(14, 6)

print("def sumas(a, b):\n\treturn a + b\n\nvalor = sumas(14, 6)\nprint(valor)")


print(valor)

print("\n::::::: Simplificando lambda :::::::\n")
print("suma = lambda a,b: a + b\n")
suma = lambda a,b: a + b    # crea la funcion anonima, sin nombre

print("print(suma(7,3))")

print(suma(7,3))

