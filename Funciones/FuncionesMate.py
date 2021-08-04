#libreria matematica
import math;

#alternar entre un numero
import random

print(math.pow(10,5)); #el primer numero es el que elavre y el segundo es el elevado
print(math.sqrt(64)); #raiz cuadrada de 64
print(math.isqrt(64)); #raiz cuadradra de 64 en negativo
print(math.sin(90)); #el seno de un angulo
print(math.cos(90)); #coseno
print(math.tan(90)); #la tangente 
print(math.factorial(10)) #el factorial de un numero, desde el 1 hasta el numero ingresado

print(random.randint(1,11)); #el segundo parametro siempre diminuye 1

lista = [1,2,3,"Hola","Adios"];
print(random.choice(lista));