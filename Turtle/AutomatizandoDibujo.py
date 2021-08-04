import turtle
from typing import Tuple;

s = turtle.Screen();
t = turtle.Turtle();

'''
#dibujar un cuadrado
t.forward(100);
t.right(90);
t.forward(100);
t.right(90);
t.forward(100);
t.right(90);
t.forward(100);'''

#automatizar el proceso de arriba 
'''for i in range(4):
    t.forward(100);
    t.right(90);'''

'''t.circle(100);
t.circle(80);
t.circle(70);
t.circle(60);
t.circle(50);
t.circle(40);
t.circle(30);
t.circle(20);'''

#automatizar el proceso de arriba
resultado = input("Quieres imprimir una figura?")
if resultado == "si":
    i = 0;
    while i <= 100:
        t.circle(i);
        i += 10;
else:
    print("oka"); 


turtle.done();