print('\n------------- GESTION DE CADENA DE TEXTO -----------------\n')
print("\t\t#############  Método isdigit()  #############\n")

cadena1 = "123"
cadena2 = "25k4l3"
num1 = "35.4"
num2 = "-45"

print(str(cadena1) + " es digito ?  ====>  " + str(cadena1.isdigit()) + "\n")
print(str(cadena2) + " es digito ?  ====>  " + str(cadena2.isdigit()) + "\n")
print(str(num1) + " es digito ?  ====>  " + str(num1.isdigit()) + "\n")
print(str(num2) + " es digito ?  ====>  " + str(num2.isdigit()) + "\n")

print("\t\t#############  Método isspace()  #############\n")

cadena3 = "Curso de Pythón"

print(str(cadena3) + " <<<< ¿Tiene espacios?  >>>> " + str(cadena3.isspace()) + "\n")
print(str(cadena3.replace(' ', '')) + " <<<< ¿Tiene espacios?  >>>> " + str(cadena3.replace(' ', '').isspace()) + "\n")
print(str("' '") + " <<<< ¿Tiene espacios?  >>>> " + str(" ".isspace()) + "\n")


print("\t\t#############  Método istitle()  #############\n")

# verifica sí es titulo
print(str(cadena3) + "  ¿Es Titulo?  ===>  " + str(cadena3.istitle()))
print(str(cadena3.title()) + "  ¿Es Titulo?  ===>  " + str(cadena3.title().istitle()))
print(str(cadena3.lower()) + "  ¿Es Titulo?  ===>  " + str(cadena3.lower().istitle()))
print(str(cadena3.upper()) + "  ¿Es Titulo?  ===>  " + str(cadena3.upper().istitle()))
print(str(cadena3.swapcase()) + "  ¿Es Titulo?  ===>  " + str(cadena3.swapcase().istitle()) + "\n")


print("\t\t#############  Método isupper()  #############\n")

print(str(cadena3) + "  ¿Es Titulo?  ===>  " + str(cadena3.isupper()))
print(str(cadena3.title()) + "  ¿Es Titulo?  ===>  " + str(cadena3.title().isupper()))
print(str(cadena3.lower()) + "  ¿Es Titulo?  ===>  " + str(cadena3.lower().isupper()))
print(str(cadena3.upper()) + "  ¿Es Titulo?  ===>  " + str(cadena3.upper().isupper()))
print(str(cadena3.swapcase()) + "  ¿Es Titulo?  ===>  " + str(cadena3.swapcase().isupper()) + "\n")

print("\t\t#############  Método join()  #############\n")

# concatena cada iteracion, ejemplo
print("cadena : " + str(cadena1) + " ===> " + str(cadena1.join("Html")) + "\n")

print("\t\t#############  Método ljust()  #############\n")
# aumenta hacia la derecha, mas de la dicmension

cadena4 = "PHP"
print(str(cadena4) + "   tiene " + str(len(cadena4)) + " elementos  <------> " + str(cadena4.ljust(10,"e")) + " contiene " + str(len(cadena4.ljust(10,"e"))) + " elementos\n")

print("\t\t#############  Método lstrip()  #############\n")
# elimina caracteres de izquierda a derecha
cadena5 = cadena3 + " Con Django y Flask desde cero"

print(str(cadena5) + " <-------> " + str(cadena5.lstrip("Cur")) + "\n")

print("\t\t#############  Método maketrans()  #############\n")

''' maketrans, ubica el caracter y reemplaza con el nuevo caracter, nos devuelve mapeado
translate, se usa para traducir el mapeo, que nos devuelve lo reemplazado con 
el metodo maketrans '''

print(str(cadena5) + " =====> " + str(cadena5.translate(cadena5.maketrans("s", "S"))) + "\n")

print("\t\t#############  Método partition()  #############\n")

# particiona o divide la cadena de texto, nos devuelve una tupla
print(str(cadena5) + " <------> " + str(cadena5.partition("jan")) + "\n")

print("\t\t#############  Método removeprefix()  #############\n")

# solo elimina del elemento que inicia la cadena, un caracter ó palabra
print(str(cadena5) + " <------> " + str(cadena5.removeprefix("Curso ")) + "\n")

print("\t\t#############  Método removesuffix()  #############\n")

# solo elimina del elemento que esten al final de la cadena, un caracter ó palabra
print(str(cadena5) + " <------> " + str(cadena5.removesuffix("ero")) + "\n")


print("\t\t#############  Método replace()  #############\n")
print(str(cadena5) + " <------> " + str(cadena5.replace("ó", "o")) + "\n")

print("\t\t#############  Método split()  #############\n")
# elimina el caracter o palabra de la cadena, nos devuelve en una lista
print(str(cadena5) + " ------ Original\n" + str(cadena5.split("de")) + "\n")

print("\t\t#############  Método splitlines()  #############\n")

cadena6 = cadena5 + "\nempezando con full@stack y\n back\nend"
# elimina los caracter especiales, nos devuelve en una lista


print(str(cadena6) + " ------ Original\n\n" + str(cadena6.splitlines()) + "\n")


print("\t\t#############  Método startswith()  #############\n")
cadena7 = "Curso de Html5\ny Css3 estaphp\r desde cero"

# Filtra el primer caracter inicial, nos devuelve booleano
# \r  ===>  remueve, y aumenta mas caracteres, sí es menor de caracter final

print(str(cadena7) + "\n")
print(cadena7.startswith("de"))
print(cadena7.startswith("Cu"))


print("\t\t#############  Método endswith()  #############\n")
# Filtra el final caracter inicial, nos devuelve booleano
print(str(cadena7) + "\n")
print(cadena7.endswith("ro"))

print("\t\t#############  Método strip()  #############\n")

# elimina los caracteres de la cadena, realizada por caracteres, de inicio
# y final

print(str(cadena5) + "  ----- Original\n" + str(cadena5.strip("Co")) + "\n")

print("\t\t#############  Método title()  #############\n")
print(str(cadena5) + "  ----- Original\n" + str(cadena5.title()) + "\n")