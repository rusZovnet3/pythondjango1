print("######################  Conversion de Velocidades  ######################\n\n")

opcion = 0
repetir = 1

while repetir == 1:
    data = input("Ecoja una de las opciones\n"
                    + "1 - Convertir mt/s  a  km/h\n"
                    + "2 - Convertir km/h  a  mt/s\n")

    if data.isnumeric():
        opcion = int(data)
        if opcion == 1 or opcion == 2:
            if opcion == 1:

                ejecutar = True
                while ejecutar:
                  value1 = input("Introduzca una velocidad en mt/s\n")
                  if value1.isnumeric() or value1.replace(".", "").isnumeric() or value1.replace("-", "").find(".") != -1 or value1.replace("-", "").isnumeric():
                    velocidad = float(value1)
                    print(f"{velocidad} mt/s = {velocidad * 3600 / 1000} km/h\n")
                    ejecutar = False  # ya no se ejecutara por consola
                    repetir = 0       # se detendra
                  else:
                    ejecutar = True
                    print("Datos incorrectos")

            if opcion == 2:
                ejecutar = True
                while ejecutar:
                  value1 = input("Introduzca una velocidad en km/h\n")
                  if value1.isnumeric() or value1.replace(".", "").isnumeric() or value1.replace("-", "").find(".") != -1 or value1.replace("-", "").isnumeric():
                    velocidad = float(value1)
                    print(f"{velocidad} km/h = {velocidad * 1000 / 3600} mt/s\n")
                    ejecutar = False  # ya no se ejecutara por consola
                    repetir = 0       # se detendra
                  else:
                    ejecutar = True
                    print("Datos incorrectos")
        else:
            print("Datos incorrectos")
    else:
        print("Datos incorrectos")