print('\n------------- TUPLES -----------------\n')
print("\t\t#############  Lista inmutable de la clase Tuple  #############\n")

lists = (1,2,"Hi",-45.3,"Himan",2,2.1,8,"Hi",2, "2")

print("\t\t\t\t#############  --------  #############\n")

print(str(lists) + " ===> cantidad de caracter 2 es: " + str(lists.count(2)) + "\n")
print(str(lists) + "  -- la posicion 3, su elemento es: " + str(lists[3]) + "\n")

print(str(lists) + " ---- mostrar la posicion 2 hasta el 5 ?\n" + str(lists[2:5]) + "\n")
print(str(lists) + " ---- mostrar la posicion 0 hasta el 4 ?\n" + str(lists[0:4]) + "\n")

# Objeto Tuple
lists1 = tuple([4,5,6])
print(lists1)


print("\n\t\t\t\t#############  tuples anidadas  #############\n")
# tuples anidadas
lists2 = (lists,lists1, 'php')

print(str(lists2) + "\n ----------------------\n")


# desglosar conjunto de tuplas

for items in lists2:
    print(items)

print("--------------\n")

for ite in lists2:
    for num in ite:
        print(num)

print("--------------\n")