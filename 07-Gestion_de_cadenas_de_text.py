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










