print('\n------------- CAPTURA DE DATOS -----------------\n')
print("\t\t#############  metodo input()  #############\n")

# permite ingresar datos, como resultado es de tipo string
# debe ingresar dato en la terminal, y presionar enter

#carga = input("Ingrese un dato : ")
#print(carga)

## se puede convertir a valores tipo entero, con datos numericos
#carga1 = int(input("Ingrese un valor numerico : "))
#print(carga1)

data = input("Ingrese un dato : ")

if data.replace("-", "").isnumeric():
  print("el valor : " + str(data) + " =====>  entero\n")
else:
    if data.replace("-", "").find(".") != -1:
        print("el valor : " + str(data) + " =====>  float\n")
    else:
        print("el valor : " + str(data) + " =====>  string\n")






