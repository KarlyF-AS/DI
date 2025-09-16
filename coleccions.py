"""Coleccións:

Listas
Tuplas
Diccionarios


"""
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