#personalizar el lienzo y lapiz

import turtle;

s = turtle.Screen();
t = turtle.Turtle();

#modificar color de fondo
s.bgcolor("blue");

#modificar el nombre del lienzo
s.title("Proyecto 1");

#modificar tamaño de la pluma
t.shapesize(10, 5, 1); #ancho, largo y borde
t.shapesize(5, 10, 1);
t.shapesize(3, 3, 3);

#modificar color de la pluma
t.fillcolor("orange");
t.forward(100);

#modificar el color de la tinta
t.pencolor("white");
t.forward(100);

t.color("green", "blue"); #primero lienzo y luego tinta
t.right(90);
t.forward(100);

#aumentar el grosor de la linea
t.pensize(5);
t.forward(100);

turtle.done();
