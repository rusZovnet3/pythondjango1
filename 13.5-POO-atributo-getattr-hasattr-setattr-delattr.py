print('\n------------- P.O.O. -- Gestion de atributos -----------------\n')
print("\n\t\t::::::: atributo - getattr() :::::::\n")

class Persona:
    name = "Lurdes"
    address = ["Calderon", "Andrade"]
    ace = 29


# identifica el atributo existente de la clase con su valor como resultado
# per = getattr(Persona, "name")  

# Sí, el atributo no existe en la clase, se añade el tercer parametro por defecto
per = getattr(Persona, "names", "El atributo no existe")
print(per)


print("\n\t\t::::::: atributo - hasattr() :::::::\n")
# verifica el atributo de la clase existente como resultado boolean

per = hasattr(Persona, "name")
print(per)

print("\n\t\t::::::: atributo - setattr() :::::::\n")
# carga un dato nuevo, al atributo especifico de la clase

setattr(Persona, "name", "Rosmery")
per = getattr(Persona, "name", 25)
print(per)


print("\n\t\t::::::: atributo - delattr() :::::::\n")
#  elimina el atributo especifico de la clase

delattr(Persona, "name")
per = getattr(Persona, "name", "Sapeee")
print(per)