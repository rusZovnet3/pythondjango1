class Animales:
    names = "Aves"
    tipo = "Terrestre"


    '''def __init__(self, value):
        self.name = value    
        self.group()
    def group(self):
        print(self.name)


animal  = Animales("Peces")
animal1 = Animales("Terrestre")'''



###  
    def __init__(self, value):
        self.name = value 

    def group(self):
        print(self.name)

animal  = Animales("Peces")
print(animal.name)     #  variable de Instancia

animal1 = Animales("Mamiferos")
print(animal1.names)    #  variable de clase




