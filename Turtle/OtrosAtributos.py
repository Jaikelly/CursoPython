
import turtle;

s = turtle.Screen();
t = turtle.Turtle();

'''#como rellenar figuras, todo el codigo que este entre begin y and es lo que se va a rellenar 
t.begin_fill(); #iniciar rellenado
t.circle(100);
t.end_fill(); # finaliza rellanado

t.begin_fill();
t.color("white", "white"); 
t.circle(50);
t.end_fill();'''

#modificar la pluma
#t.shape("classic");
#t.shape("circle");
#t.shape("square");
t.shape("turtle");

#levantara la pulma y dejara de pintar
t.penup();
t.forward(100);

#volvera a dibujar
t.pendown();
t.forward(100);

#deshacer(ctrl + z)
t.undo();

#se limpia toda la pantalla pero la pluma queda en el mismo lugar
t.clear();

#el programa se reinicia por completo
t.reset();

t.forward(100);
#deja un sello
t.stamp();
t.forward(100);


turtle.done();