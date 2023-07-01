def cadenas():
    cadena = input("Ingrese la cadena de texto\n")
    value = may_min(cadena)

    if len(value[0]) > 0:
        print(f"Las letras Mayúsculas son : {value[0]}")

    if len(value[1]) > 0:
        print(f"Las letras Minúsculas son : {value[1]}")

def may_min(cadena):
    mayuscula = []
    minuscula = []

    for item in cadena:
        if item.isupper():      # sí la cadena esta en mayuscula
            mayuscula.append(item)
        else:
            minuscula.append(item)

    return [mayuscula,minuscula]    # retornar con una coleccion de objetos


cadenas()