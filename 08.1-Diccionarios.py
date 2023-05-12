print('\n------------- DICCIONARIO -----------------\n')
print("\t\t#############  -------  #############\n")

data = {"nombre": "Marisol", "apellido": "Mendoza Cabrera", "edad": 31}
print(data['edad'])


print("\n\t\t#############  creacion de diccionario  #############\n")
data1 = dict((("pais", "Bolivia"), ("sexo", "Femenino")))
print(data1)


print("\n")
# otro modo de crear diccionario, con datos numericos
data2 = dict(estatura=-185,densidad=100.4)
print(data2)

print("\n\t\t#############  metodo get()  #############\n")
# muestra el valor, si no existe?, lo omite

print(data2.get('densidad', 'Existe'))  # muestra el valor, pero no muestra el siguiente 
                                        # parametro
print(data2.get('altura', 'no existe'))  # lo omite 


print("\n\t\t#############  metodo items()  #############\n")

# muestra una coleccion de Tuplas

print(data.items())

print("\n\t\t#############  metodo keys()  #############\n")
print(str(data) + "   --- Original\n")
print(data.keys())

print("\n\t\t#############  metodo values()  #############\n")
print(str(data) + "   --- Original\n")
print(data.values())

print("\n\t\t#############  metodo clear()  #############\n")
# vacia los elementos de la tupla
#print("data = " + str(data) + " ----> metodo data.clear() ==> " + str(data.clear()) + "\n")
data3 = data.copy()
data3.clear()
print(data3)

print("\n\t\t#############  metodo copy()  #############\n")


print("data = " + str(data) + " ---- Original \nnuevo = " + str(data.copy()) + "\n")

print("\n\t\t#############  metodo dict.fromkeys(x, y)  #############\n")

print("val2 = dict.fromkeys(['a', 'b', 'c', 'd'], 1) ===> " + str(dict.fromkeys(['a', 'b', 'c', 'd'], 1)) + "\n")

print("\n\t\t#############  metodo pop()  #############\n")
data4 = data.copy()

# este metodo elimina la variable, mostrando el valor eliminado

print("data4 = " + str(data) + "   ---- Original\teliminar el nombre\nnuevo = data4.pop('name')  ==>  " + str(data4.pop("nombre")) + "\ndata4 = " + str(data4) + "\n")

print("\n\t\t#############  metodo popitem()  #############\n")
# este metodo elimina las variable ultima, mostrando la primer variable y su valor intacto
data5 = data.copy()


print("data5 = " + str(data) + "   ---- Original\nnuevo = data5.popitem()  ==>  " + str(data5.popitem()) + " \t---- variable y su valor eliminado\ndata5 = " + str(data5) + " \t--- resultado\n")


print("\n\t\t#############  metodo setdefault()  #############\n")

# * permite mostrar el valor, asignando la variable seleccionada al metodo
# * Sí no lo existe la variable asignada al metodo, asigna la variable como nueva,
# al diccinario
data6 = data.copy()

print("Buscar la variable apellido ?\n")
print("data6 = " + str(data6) + "  ----- Original")

valor6 = data6.setdefault("apellido")

print(str(valor6) + " ---- Resultado\n \t\t:::::::::::::::::::::\nMostrar la variable sexo ?\n")

data7 = data.copy()
print("data7 = " + str(data7) + " \t----- Original")

valor7 = data7.setdefault("sexo")

print("valor7 = data7.setdefault('sexo')  \t------>  " + str(valor7) + "    ===> No existe la variable sexo")

print("data7 = " + str(data7) + "  --- Resultado\n como no existe la variable << sexo >> , se agrego la variable al diccionario data7\n")

print("\n\t\t#############  metodo update()  #############\n")
# *Permite actualizar los valores, si las variables son iguales del diccionario
# *Sí no existe la variable, se lo asigna al diccionario con la variable y su valor

data8 = data.copy()
print("data8 = " + str(data8) + "  \t----- Original")
print("data1 = " + str(data1) + "  \t------ lo que remmplazaré al data8\n")

data8.update(data1)

print("data8.update(data1)  ------ metodo para cambiar el diccionario\n")
print("\t Resultado, como no existe la variable, se lo asigno al diccionario")
print("data8 = " + str(data8) + "\n")

print("\t\t :::::::::::::::::::::\n\t\t Original")
data9 = {"nombre": "Monica Patrica", "pais": 'Rusia', "apellido": "Zurita Lino", "edad": 30}

print("data8 = " + str(data8) + "\n\t\t Actualizar")
print("data9 = " + str(data9) + "\n")

data8.update(data9)
print("data8.update(data9)  ------ metodo actualizar\n\t\tResultado")
print("data8 = " + str(data8) + "\n")


print("\n\n\nPara recorrer los valores del diccioario data8\n")
for itemm in data8:
    print(data8[itemm])
