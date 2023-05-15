print('\n------------- FUNCIONES -----------------\n')
#print("\t\t#############  número fijo de parametros #############\n")

'''print("\n----------------- sin parametros  ------------------------\n")
def ejecutar():
    print("Hola")

print("def ejecutar():\nprint('Hola')\n\nejecutar()\n")

ejecutar()'''

''''print("\n------------------ con parametros N°1 ---------------------\n")
def ejecutar1(data):
    print(data)

print("def ejecutar(data):\nprint(data)\n\nejecutar('Hola Mundo')\n")

ejecutar1('Hola Mundo')'''

'''print("\n------------------ con parametros N°2 ---------------------\n")
def ejecutar2(data):
    return data

valor = ejecutar2("Marisol")

print("def ejecutar(data):\nreturn data\n\nvalor = ejecutar('Marisol')\nprint(valor)\n")

print(valor)'''


'''print("\n------------------ con parametros N°3 ---------------------\n")
def ejecutar3(data, age):
    return f"Mi nombre es : {data}\ny mi edad es de : {age}\n"

print("def ejecutar(data, age):\n\treturn f'Mi nombre es : {data} y mi edad es de : {age}'\n\nprint(ejecutar('Lurdes', 29))\n")

print(ejecutar3("Lurdes", 29))'''

#print("\t\t#############  con parametros con valores por defecto #############\n")

'''print("\n------------------ con parametros N°1 ---------------------\n")



# parametro, coleccion de argumentos, que devuelve en una tupla
def funcion(*values):
    # print(values)    # Mostrar todos los elementos en una tupla
    # print(values[1])    # Mostrar el elementos de la posicion de la coleccion de datos
    for itemm in values:
        print(itemm)    # Muestra los elementos desglosados

val2 = 45
funcion(20, "JImena", 40, val2)'''


'''print("\n------------------ con parametros N°2 ---------------------\n")
# valor por defecto en parametros, debe ser al final, el parametro por defecto

def ejecutar4(data, edad, est = 30):
    return f"Mi nombre es {data} y mi edad es de {edad} años\n"


print(ejecutar4("Lurdes Calderón Andrade", 29))'''

'''print("\n------------------ con parametros N°3 ---------------------\n")
# 

def ejecutar5(data, est = 30, edad = 100):
    return f"Mi nombre es {data} y mi edad es de {edad} años, con uns estatura de {est}\n"


# *esto permite, si no asignamos los parametros de defecto a la ejecución
# se ejecutara mostrando los valores por defecto de los parametros
# *Sí asignamos parametros a la ejecución, a los de defectos, cambiara el datos,
# segun el parametro correspondiente
print(ejecutar5("Lurdes Calderón Andrade"))'''


'''print("\n\t------------------ con parametros N°4 ---------------------\n")
# Practica

def alumnos_aprobados(aprobados, **aulas):
    total = 0
    for alumnos in aulas.values():
        total += alumnos
    return (aprobados * 100 / total, "porcentaje de alumnos aprobados")

# 50 aprobados
# A, B, C son valores de cantidad de alumnos

valor = alumnos_aprobados(50, A = 22, B = 30, C = 26)  # es el porcentaje de alumnos 
                                                       # que aprobaron las tres aulas
#print(valor)  # devuelve en Tupla
print(f"{valor[0]} {valor[1]}")'''

     
print("\t\t#############  con parametros nombrados y los no nombrados #############\n")
print("\n\t------------------ con parametros N°1 ---------------------\n")
# Practica
# *los parametros de la izquierda son: parametros no nombrados
# *los parametros de la derecha despues de la barra son: parametros nombrados

def funcion2(a, b, c, /):
    print(a, b, c)

funcion2(20, 35, 8)

print("\n\t------------------ con parametros N°2 ---------------------\n")
# parametro nombrado, 

def funcion3(a, b, /, c, d):
    print(a, b, c, d)

# funcion3(c=45, 90, 35)  # error, respetando el orden de asignacion de parametros nombrados

#funcion3(90, 35, c=17, d='Rosa')
funcion3(90, 35, d='Celia', c=32) # el orden , para los parametros nombrados, no importa

