class Animales:
    name = "Aves"
    tipo = "Terrestre"

    # self  -->  invoca los atributos dentro de la clase
    #  nombre de la clase
    # parametro variable value

    def __init__(self, value):
        self.name = value    
        self.group()

    def group(self):
        print(self.name)



# Objeto
animal = Animales("Aerea")


# 1:58