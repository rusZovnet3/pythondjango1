nombre = "Maria VictorIa Orellana Meyui"    
edad = 30


#print(f"Mi novia se llama {nombre + ' Orellana Meyui'} y tiene {edad} años, y gana {edad * 20} Bs.")

#print("Mi novia se llama {} y tiene {} años" .format(nombre,edad))

#print(nombre.capitalize())    # Devuelve la primera letra en mayuscula
#print(nombre.casefold())     # Devuelve en minuscula
#print(nombre.center(14, '0'))       ej:  "Hola Mundo" ==>  "00Hola Mundo00"

#print(nombre.count("a"))     # muestra la cantidad de caracter especifico
#print(nombre.count("a",3))    # caracter, posicion de 1 a n
#print(nombre.count("a",1,7))    # caracter, posicion inicio, posicion fin
#print(nombre.startswith("M"))    # devuelve false, true,   con caracter inicial de la cadena
#print(nombre.startswith("a",2,7))   # caracter, posicion ini, posicion fin ==> con caracter inicial de la cadena



#print(nombre.endswith("a"))  # Devuelve false, true  ==>  con caracter final de busqueda
#print(nombre.endswith("a",10,14))  # empieza a buscar desde la derecha a izquierda, (caracter, posicion ini, posicion fin)

#print(nombre.expandtabs(2))     # aumenta la °n espaciado veces, dependiendo de caracteres especiales. por ej:  \t   que se convierte en espacio


#print(nombre.find("Orellana",15))  # busca la palabra, como resultado busca la posicion

#nom1 = "Rosio Pedraza Zabala"
#edad1 = 40
nom2 = "Anahi\tColque\tUrquieta"
edad2 = 29


#print(nom2.expandtabs(1))
#print(nom2.find("Colque"))
print('--------- metodo format() -----------------')
cadena = "mi nombre es {0} y tengo {1} años".format(nom2.expandtabs(1),edad2)
print(cadena + '\n')


# metodo diccionario
print('--------- metodo format_map() -----------------')
point = {'x':41, 'y':55, 'z':50}
print('{x} {y} {z}'.format_map(point))


# metodo realizar busqueda
nom3 = "Lurdes Calderon Andrade alias Lulu con insignia de 69"
edad3 = 28
print('\n')

# index ==>   realiza la busqueda de la posicion de la palabra
print('--------- metodo index() -----------------')
data = nom3.index("alias", 0, len(nom3))
print(str(data) +'\n')

# Verifica sí es numero y letras en la cadena, pero que no contenga caracteres especiales,
# ej: los espacios.
print('--------- metodo isalnum() -----------------')
data1 = nom3.replace(' ', '').isalnum()
print(nom3.replace(' ', '') + ' ==> ' + str(data1))
print('\n')


# Verifica si el alfabetico de la cadena, pero que no contenga espacios
print('--------- metodo islpha() -----------------')
data2 = nom3.replace(' ', '').isalpha()
print(nom3.replace(' ', '') + ' ==> ' + str(data2))
print('\n')


# verifica si es número entero, en una cadena
print('--------- metodo isnumeric() -----------------')
data3 = str(edad3).isnumeric()
data4 = str(edad3 - 30).isnumeric()
data5 = str(edad3 / 25).isnumeric()

print(str(edad3) + ' ==> ' + str(data3) + '\n')
print(str(edad3 - 30) + ' ====> ' + str(data4) + '\n')
print(str(edad3 / 25) + ' ===> ' + str(data5) + '\n')


# verifica si es número entero, en una cadena
print('--------- metodo isdecimal() -----------------')
data3 = str(edad3).isdecimal()
data4 = str(edad3 - 30).isdecimal()
data5 = str(edad3 / 25).isdecimal()

print(str(edad3) + ' ==> ' + str(data3) + '\n')
print(str(edad3 / -25) + ' ====> ' + str(data4) + '\n')
print(str(edad3 / 25) + ' ===> ' + str(data5) + '\n')


# verifica si la cadena estan en minusculas
print('--------- metodo islower() -----------------')
cadena6 = "las palabras estan en minusculas"

data6 = cadena6.islower()
print(cadena6 + ' ---->  ' + str(data6) + '\n')
print(nombre + ' -----> ' + str(nombre.islower()) + '\n')

# verifica si la cadena estan en mayusculas
print('--------- metodo isupper() -----------------')
cadena7 = "ES MAYUSCULA"

data7 = cadena7.isupper()
print(cadena7 + ' ---->  ' + str(data7) + '\n')
print(cadena6 + ' -----> ' + str(cadena6.isupper()) + '\n')
print(nombre + ' -----> ' + str(nombre.isupper()) + '\n')


