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
s,m = funcionSumaMedia(var)
_,m = funcionSumaMedia(var)
s,_ = funcionSumaMedia(var)
print(m)
#Si quiero que solo se muestre un solo valor (ej. m) a la funcion en vez de pasarle s,m, hago: _,m (la barra baja sustituye el valor de s y no se muestra por pantalla)



#Excepciones
class ErroIdade (Exception):
    def __init__(self,edade):
        self.edade = edade
    def __str__(self):
        return "Erro edade inadecuado: " + str(self.edade) + "incorrecta"
class Persoa4:
    """Clase para definir unha persoa"""
    def __init__(self, nome, dni, idade):
        self.nome = nome
        self.dni = dni
        self.idade = self.comprobarIdade(idade)

def comprobarIdade(self, id):



def division (a,b):
    return a/b
try :
    division(1,1)
    print("El resultado de la division es: ", division(5,4))
except ZeroDivisionError:
    print("Operacion abortada: non se pode dividir por cero")

n1 = 1
n2 = str(2) + "Texto"
resultado = 0
try :
    division(n1,n2)
except (ZeroDivisionError, TypeError) as e:
    print("Erro o facer a division: " + str(e))
else: print("O resultado da operacion e: " + str(resultado))