print('\n------------- P.O.O. -----------------\n')
print("\n\t\t::::::: metodo  __del__()   -- destructor :::::::\n")

class Persona:

    def __init__(self, name):
        self.name = name

    def grupo(self):
        print("Nombre del grupo", self.name)

    def __del__(self):
        self.name = "Rosmery"
        print("Se ha destruido")

per = Persona("Lurdes")
per.grupo()

#  del per      ===>  elimina el objeto 

print(per.name)


#  el metodo destructor, se ejecuta al ultimo, despues del los metodos de resultado