import turtle;

s = turtle.Screen();
t = turtle.Turtle();

#linea de 100 px
t.forward(100);
t.right(90);
t.forward(200);

#me retornara la ubicacion exacta donde esta dicho objeto(pluma)
print(t.pos());


turtle.done();

