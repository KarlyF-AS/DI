#Funcions
def nome_da_funcion (parametro1, parametro2):
    """Instrucciones da función
       que procesan os parámetros"""
    print(parametro1)
    print(parametro2)
#range(start = 3, stop = 5, step = 4)

nome_da_funcion(3, "Ola")
nome_da_funcion(parametro2= 4.5, parametro1= "Creo que era como se chamaba")
def repetir_mensaxe  (mensaxe, veces = 1):
    print(mensaxe + veces)
    repetir_mensaxe("Ola", 5)
    repetir_mensaxe(" Adeus")

def repetir_mensaxes (mensaxe, veces = 1, *  maisMensaxes):
    print(type(maisMensaxes))
    print("Os parámetros extra son: " + str(len(maisMensaxes)))
    print (mensaxe * veces)
    for outraMensaxe in maisMensaxes:
        print(outraMensaxe * veces)
repetir_mensaxes("Ola", 4, "Chao", "Adeus", " Arivederchi", "Goodbye")
repetir_mensaxes("Ola", 5)

def persoa (nome, dni, **maisDatos):
    print ("O nome é:" + nome)
    print("O DNI é: " + dni)
    for variable in maisDatos.keys():
        print("O ", variable , "é: " , maisDatos[variable])

persoa("Karly", "12345J", edade = 21, altura = 1.57, conSueño= True)

var = [1,2,3]
def funcion (parametro):
    parametro[0] = 3
    parametro[1] = 4
    parametro[2] = 5
funcion(var)

print(var)

def funcionSuma (lista):
    suma = 0
    for num in lista:
        suma = suma + num
    return  suma
print(funcionSuma(var))

def funcionSumaMedia (lista):
    suma = 0
    for num in lista:
        suma = suma + num
    return suma, suma/len(lista)
tupla = funcionSumaMedia(var)
print(tupla)

#Si quiero que solo se muestre un solo valor (ej. m) a la funcion en vez de pasarle s,m, hago: _,m (la barra baja sustituye el valor de s y no se muestra por pantalla)