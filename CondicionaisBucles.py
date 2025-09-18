#Sentencia condicionais
n1 = 3
if n1 > 5 :
    print("Pois resulta")
    print("que n1 é")
    print("maior que 5")
else:
    if n1 == 0:
        print("n1 é")
        print("igual a 0")
    else:
        print("Pois resulta")
        print("que 1 é")
        print("menor que 5")

if n1 > 5 :
    print("Pois resulta")
    print("que n1 é")
    print("maior que 5")
elif n1 == 0:
    print("n1 é")
    print("igual a 1")
elif n1 == 1:
    print("n1 é")
    print("igual a 2")
else:
    print("Pois resulta")
    print("que n1 é")
    print("menor que 5")


#Bucles
while n1 < 11 :
    print(n1)
    n1 += 1

n1= 0
while True:
    print(n1)
    if n1 == 10:
        print("True")
        break
    else:
        print("False")
    n1 += 1

#ejemplo del bucle for in
numeros = [1,2,3,4,34566,7,8,9,10,11,12,13,14]
print(numeros)
suma = 0
for numero in numeros:
    print(numero)
    suma += numero
print(suma)

#ejemplo con diccionarios
d= {1: "UN", 2: "DOUS", 3:"TRES"}
for clave in d:
    print(d[clave])

for indice in range(3,10,3):
    #print(indice)
    print(numeros[indice])

"""
for (int i = 0; 1<5; i++){
    System.out.println (i);
    System.out.rprintln (numeros [i];)
}
"""