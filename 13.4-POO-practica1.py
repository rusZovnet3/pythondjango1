class Animales:
    aves = ["Flamenco", "Guacamaya", "Avestruz"]
    mamifero = ["Perro", "Leon", "Tigre", "Lobo", "Elefante", "Oveja"]
    pez = ["Tiburon", "Ballena", "Delfin", "Pejerrey", "Sabalo", "Salmon"]

    def __init__(self):
        self.group()

    def group(self):
        start = True
        while start:
            value = input("Ingrese el nombre de un animal\n")
            opcion = input("Seleccione un grupo de animal\n"
                        + "1 - aves\n"
                        + "2 - mamiferos\n"
                        + "3 - peces\n")

            if opcion == "1":
                ejecutar = True
                cont = 0
                ave = True

                while ejecutar:
                    while len(Animales.aves) > cont:
                        if Animales.aves[cont] == value:
                            ejecutar = False
                            start = False
                            print(f"La ave {Animales.aves[cont]} está en el grupo de aves")
                            break
                        else:
                            cont+=1
                    else:
                        ejecutar = False
                        run = True
                        print("El animal no está registrado")

                        while run:
                            opcion = input("Sí desea seguir buscando, seleccione una de las siguiente opciones\n"
                                + "y\n"
                                + "n\n")

                            if opcion == "y" or opcion == "n":
                                run =  False
                                start = True if opcion == "y" else False
                            else:
                                print("Datos incorrectos")
                                run = True
                                


animal = Animales()