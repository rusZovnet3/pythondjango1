print('\n------------- COLECCION DE DATOS -----------------\n')
##  Lista


colecc = ["J",1,3,"im",5,"na","e",7,"Celia",9,2,"W",4,6,8]
numeros = [1,3,5,7,9,2,4,6,8]


nombres = list(["Jimena","Gabriela","Blanca","Isabel","Lurdes","Rosa","Anahi","Rosio"])


count = len(numeros)

print(f"{str(numeros)} ---------> {count} elementos\n")
print(f"La posicion 5, obtengo el elemento ---> {numeros[5]} \n")
print(f"El elemento {numeros[5]} su posicion es ----> {str(numeros.index(numeros[5],0,len(numeros)))}\n")

# Ordenar numeros
print("-----Ordenando numeros-------\n")
numeros.sort()

for item in numeros:
    print(item)

# revertir numeros
print("\n-------Revertir números------\n")
numeros.sort(key=None,reverse=True)

for item in numeros:
    print(item)

# ordenar alfabeticamente
print("\n------Ordenar por alfabetico------\n")

nombres.sort()
for nom in nombres:
    print(nom)

print("\n ============================================================================\n")
print("\t\t#############  agregar elementos a un arreglo  #############\n")

campo1 = [3,2,2,1,9,9,4,30,3]
print(campo1)
campo1.append(12)
print(campo1)
campo1.append(colecc[8])
print(campo1)

print("\n\t\t#############  agregar elementos a un arreglo por posicion  #############\n")

campo1.insert(3, nombres[1])
print(campo1)

print("\n\t\t#############  remover elementos de un arreglo  #############\n")

campo1.remove(9)
print(campo1)

print("\n\t\t#############  elimina elementos a un arreglo por posicion  #############\n")

# elimina el ultimo elemento por default
campo1.pop()
print(campo1)


# por posición
campo1.pop(4)
print(campo1)

print("\n\t\t#############  agregar multiple elementos a un arreglo   #############\n")

campo1.extend(["Viky", 28, -4.5])
print(campo1)

print("\n\t\t#############  ordena los elementos del arreglo   #############\n")

num2 = [78,14.19,5,7,80,32]
val2 = sorted(num2)

print(val2)

print("\n\t\t#############  unir array anidada a una lista   #############\n")

listsi = []
data1 = [1,2,3]
data2 = [4,5,6]

print(listsi)

#listsi.append(data1)
#listsi.append(data2)

listsi.insert(1, data1)
listsi.insert(0, data2)


print(listsi)

# mostrar un elemento 2
print("\nMostrarme el elemento 2 ?\n")
print(listsi[0][1])

print('\n')

for iitem in listsi:
    #print(iitem)
    for ival in iitem:
        print(ival)


print("\n\t\t#############  vaciar datos de un array   #############\n")

# eliminar todos los elementos del array
datos1 = [154,2,0,54,78,36]
datos3 = [15,4,12.44,10,56,74,6,51,"Hola",45]

print(str(datos1) + " ==> " + str(datos1.clear()))

print("\n\t\t#############  copiar datos de un array a otro nuevo   #############\n")

datos2 = datos3.copy()

print(f"datos3 = " + str(datos3) + " <====> datos2 = " + str(datos2))

print("\n\t\t#############  mostrar desde la posicion especifica hasta otra posicion   #############\n")

# mostrar la posicion especifica hasta la posicion final
#print(datos2[3:])

# mostrar la posicion inicial hasta la posicion final
#print(datos2[3:8])

print(datos2[:5])

print("\n\t\t#############  eliminar elementos, por posiciones ini y fin   #############\n")

# eliminar un elemento del array, por posicion
print(str(datos2) + " verificar con el de abajo\n")

del datos2[3]
print(datos2)

# eliminar elementos por posicion ini y fin
print("\n" + str(datos2) + " verificar con el de abajo, elimine la posicion 3 y 5\n")

del datos2[0:3]
print(datos2)

print("\n\t\t#############  eliminar todos los elementos   #############\n")

del datos2[:]
print(datos2)

print("\n\t\t#############  mostrar en posicion ini y fin, en n saltos de elementos   #############\n")

print(str(datos3) + " Verificar ")
print(datos3[0:6:2])

print("\n ----------------- \n")



datos4 = ["World","Mundo", "menor",-14,10.1,-3.05,124,"python"]
datos5 = [23,"css",-45.4,"html","c#"]
datos6 = [15,36.1,-3.45]
datos7 = ["javascript", "angular", "vue", "react", "ionic", 45]
datos8 = ["php", "mysql", "mongoDB", "oracle", "sqlite"]
num11 = 45
num12 = 65
num13 = "C++"
num14 = -1
datos9 = ["kubernetes", "docker",[154, [25, "appserv"], "25"] , "xampp", 2002, ["github"], "git"]

datos3.append(datos8)
datos6.append(num11)
datos6.append(datos5)
datos6.append(num13)
datos3.append(num13)
datos3.append(datos7)
datos3.append(datos6)
datos3.append(num13)
datos3.append(num14)

print(str(datos3)+ "  \n\nverificar \n\n")
print("El mejor lenguaje de programación es : " + str(datos3[12][0]) + "\n")
print("El lenguaje de programación el que uso es : " + str(datos3[13][4][4]) + "\n")
print("No me gusta usar las sintaxis de : " + str(datos3[13][5]) + "\n")



