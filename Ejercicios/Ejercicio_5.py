#importacion de una galeria que ayuda en operaciones matematicas 
from math import sqrt #sqrt sacara la raiz cuadrada 

a = int(input("Ingrese el valor de a: "));
b = int(input("Ingrese el valor de b: "));
c = int(input("Ingrese el valor de c: "));
x1 = 0;
x2 = 0;

if ((b ** 2) - (4 * a * c)) < 0: #si es menor a 0, osea negativo no se puede resolver(porq no tendra raiz)
    print("No se puede realizar")
else:
    x1 = (-b + sqrt((b ** 2)-(4 * a * c))) / (2 * a)
    x2 = (-b - sqrt((b ** 2)-(4 * a * c))) / (2 * a)
    print("La solcuion es: \n x1= ", x1, "\n x2= ", x2)
    