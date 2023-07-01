print('\n------------- Iteradores y Generadores-----------------\n')
#print("\n::::::: funcion normal :::::::\n")

lista = [1,2,3,4,5]

#for item in lista:
#    print(item)

#for item in "Python":
#    print(item)

print("\n::::::: Objeto Iterador  --  iter() :::::::\n")

iterador = iter(lista)
# metodo  __next__()   ==== >  recorre

print("\n\t\t::::::: Metodo __next__() :::::::\n")

#  print(iterador.__next__())
#  print(iterador.__next__())

#while True:
#    print(iterador.__next__())

print("\n\t\t::::::: Metodo __iter__() :::::::\n")

iterador1 = lista.__iter__()

#  __sizeof__()   es la cantidad de memoria que se puede almacenar (byte)


#print(iterador1.__sizeof__())

cont = 0

while True:
    if cont < 5:
        print(iterador1.__next__())
    else:
        break
    cont+= 1







