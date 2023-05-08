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


# Carpeta 7, video 4
