print('\n------------- Iteradores y Generadores-----------------\n')
print("\n::::::: Convertir de Tupla a Obj Iterador :::::::\n")

lista = [1,2,3,4,5]

valores = ("Python", True, "PHP", 5,10.9)

dic = dict(python="Python", value=True, pdhn="PDHN", name="Lourdes")


print("\n\t\t::::::: metodo __iter__() - de forma ordenada :::::::\n")

# convierte los valores Tupla a iterador( metodo __iter__() )
iterador = valores.__iter__()

cont = 0

while True:
    if cont < 5:
        print(iterador.__next__())
    else:
        break
    cont+= 1


print("\n\t\t::::::: metodo __reversed__() - de forma al revez :::::::\n")
#  este metodo  __reversed__()  puede ser convertido de una lista inmutable, no Tupla


iterador1 = lista.__reversed__()

cont1 = 0

while True:
    if cont1 < 5:
        print(iterador1.__next__())
    else:
        break
    cont1+= 1

print("\n\t\t::::::: de diccionario al metodo __reversed__() - de forma al revez :::::::\n")

# de lista inmutable a diccionario

# iterador1 = iter(dic.values())    # values() => los valores del diccionario
iterador1 = iter(dic.items())     # items()  => la variable y sus valores


cont2 = 0

while True:
    if cont2 < 4:
        print(iterador1.__next__())
    else:
        break
    cont2+= 1

