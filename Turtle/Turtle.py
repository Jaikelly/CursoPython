import turtle;

#creamos un objeto(pantalla)
s = turtle.Screen();
#la pluma
t = turtle.Turtle();

'''
#hace una linea de xxx pixeles, se mueve a la izquierda
t.backward(100);

#se mueve hacia la derecha(se voltea la pluma)
t.right(90);

#hace una linea hacia abajo
t.forward(100);

#se mueve a la izquierda(la pluma)
t.left(90);

t.forward(100);
'''
#abreviado
t.fd(100);
t.rt(90);
t.fd(100);
t.lt(90);
t.bk(100);

#hara queda pantalla se quede fija, que no se cierre 
turtle.done();