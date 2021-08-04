import turtle;

s = turtle.Screen();
t = turtle.Turtle();

#velocidad de la pluma
t.speed(10); #del 1 al 10

#figura predefinida circulo
t.circle(10); #diametro

t.speed(10);
t.circle(50);

#punto, circulo relleno
t.dot(30); #le psamos diametro

#no se muestre la pluma
t.hideturtle();

t.speed(1);
t.circle(40);

#ver la pluma de nuevo
t.showturtle();
t.circle(60);

#moviliza la tortuga en el eje x, mantiene el eje y
t.setx(100);

#al reves 
t.sety(-100);

turtle.done();