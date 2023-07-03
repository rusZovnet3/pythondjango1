print('\n------------- P.O.O.-----------------\n')
print("\n\t\t::::::: Metodo __init__() :::::::\n")

class Animales:
    name = "Aves"

    def __init__(self):
        self.name = "Peces"    # el atributo name inicializa con nuevo valor

    def group(self):
        print(self.name)



# Objeto
animal = Animales()
animal.group()

print("\n\t\t::::::: ----- :::::::\n")
# 


class Animales1:
    name = "Aves"
    tipo = "Terrestre"

    def __init__(self):
        self.name = "Peces"    # el atributo name inicializa con nuevo valor
        Animales1.group()

    def group():
        print(Animales1.name)



# Objeto
animal1 = Animales1()