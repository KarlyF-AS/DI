"""Coleccións:

Listas
Tuplas
Diccionarios


"""
from httplib2.auth import authentication_info

# Listas

l = [23, 25, 3, -15, [23,3,34.5], "unha cadea"]
print(type(l))
"""l[4] = "outra cadea"
l[6] = [1,2,3,4]"""

print (l [-2][2])

#Slicing -----> nomeLista [Inicio:fin:salto]
print (l[2 : 5])
print (l[:5])
print (l[2:])
print (l[1:6:2])
print(l[::-1])
print(l)

#Tuplas
t= (2,5,2+4j, "Un texto", [22,3,5,6],3,9)
#t [2] = "Outra texto"
t[4][2] = "Cinco"
t2= 3,4,5,6, None
print(t2)


#Diccionarios
d = {1: "Un",
     2: "Dous",
     3: "Three",
     4: "Catro"}

print (d[3])

l2 = [1,2,3]
t2 = (1,2,3)

d2 = {1:"I", 2:"II", 3:"III"}
d3 = dict()

l2.append([3,2,1])
print (l2)




def sauda() :
     print("Ola")


sauda()
require_autenticacion(sauda)()

def log (ficheiro_log):
     def decorador_log(func):
          def decorador_funcion (*args, **kargs):
               with open(ficheiro_log, 'a') as ficheiro_aberto:
                    saida = func(*args, **kargs)
                    ficheiro_aberto.write (f"{saida}\n")
          return decorador_funcion()
     return decorador_log
