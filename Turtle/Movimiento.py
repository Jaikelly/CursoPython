import turtle;

s = turtle.Screen();
t = turtle.Turtle();

#ir, en donde queremos la pluma por medio de valores(plano cartesiano)
t.goto(100,100);
t.goto(-100,100);
#lo lleva a donde empezo (0,0)
t.home();

t.forward(100);
t.right(90);
t.forward(100);
t.right(90);
t.forward(100);
t.right(90);
t.forward(100);

turtle.done();