filas = [1]
numero = 6
expansion = ""
valor = numero

expansion = "\t".expandtabs(valor + 1)
print("{} {}".format(expansion, filas))

for i in range(1,numero):
    lon_natigua = len(filas)
    fila_nueva = [1]
    for j in range(0,lon_natigua -1):
        calculo = filas[j] + filas[j+1]
        fila_nueva.append(calculo)
    fila_nueva.append(1)
    expansion = "\t".expandtabs(valor)
    valor -= 1
    print("{} {}".format(expansion, fila_nueva))
    filas = fila_nueva
