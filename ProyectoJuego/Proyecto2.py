import turtle;
import time; 
import random;

#el movimeinto tendra un retrasa de 0.1 segundos 
retraso = 0.1;

#marcador, puntos que se lleva
contador = 0;
marcador_alto = 0;

#venta
s = turtle.Screen();
s.setup(650, 650); #le da un pixelado a la pantalla
s.bgcolor("black"); #color pantalla
s.title("Culebrita");

#jugador(serpiente)
serpiente = turtle.Turtle();
serpiente.speed(2); #velocidad de movimiento 
serpiente.shape("square");
serpiente.penup(); #no dibuje linea
serpiente.goto(0,0);
serpiente.direction = "stop"; #cuando toque la pantlla se reinicia pero la serpiente se queda en el 0,0
serpiente.color("green");

#comida
comida = turtle.Turtle();
comida.shape("circle");
comida.color("red");
comida.penup();
comida.goto(0,100); #posicion inicial
comida.speed(0);

#cuerpo
cuerpo = [];

#marcador
texto = turtle.Turtle();
texto.speed(0);
texto.color("white");
texto.penup();
texto.hideturtle();
texto.goto(0, 260);

#sirve para mostrar mensaje sinnecesidad que la turtuga dibuje cada uno
texto.write("Marcador: 0\t Marcador más alto: 0", align="center", font=("verdana", 15));


def arriba():
    serpiente.direction = "up";

def abajo():
    serpiente.direction = "down";

def derecha():
    serpiente.direction = "right";

def izquierda():
    serpiente.direction = "left";

#funcion de movimiento, movimiento a donde ira la serpiente 
def movimiento():
    if serpiente.direction == "up": #si la srpiente va hacia arriba
        y = serpiente.ycor(); #devueve la ubicacion del eje y en el objeto
        serpiente.sety(y + 20); #se mueve en el eje y
    if serpiente.direction == "down": #si la srpiente va hacia abajo
        y = serpiente.ycor(); #devueve la ubicacion del eje y en el objeto
        serpiente.sety(y - 20); #se mueve en el eje -y
    if serpiente.direction == "right": #si la srpiente va hacia derecha
        x = serpiente.xcor(); #devueve la ubicacion del eje y en el objeto
        serpiente.setx(x + 20); #se mueve en el eje x
    if serpiente.direction == "left": #si la srpiente va hacia izquierda
        x = serpiente.xcor(); #devueve la ubicacion del eje y en el objeto
        serpiente.setx(x - 20); #se mueve en el eje -x

#teclas del teclado
s.listen(); #pone a escuha la pantalla, cuando yo presione la tecla asimilara dicha tecla y hara la funcion adignada
s.onkeypress(arriba, "Up"); #tecla presionada, "hace referencia a la tecla o flecha arriba"
s.onkeypress(abajo, "Down");
s.onkeypress(derecha, "Right");
s.onkeypress(izquierda, "Left");
    

#movimiento a la serpiente repetitivo(loop) 
while True:
    s.update(); #actualizar la pantalla, se mostrara la serpiente en movimiento

    #si la cabeza de la serpiente toca el borde pierde 
    if serpiente.xcor() > 300 or serpiente.xcor() < - 300 or serpiente.ycor() > 300 or serpiente.ycor() < - 300:
        time.sleep(2);
        for i in cuerpo: #recorrera toda la lista y eliminara
            i.clear();
            i.hideturtle();
        serpiente.home(); #la serpiente vuelve al 0,0
        serpiente.direction = "stop"; #se queda en stop hasta que presionemos otra tecla 
        cuerpo.clear(); #impiamos la lista 

        #actualiza el marcador donde estaba 
        contador = 0;
        texto.clear();
        texto.write("Marcador: {} \t Marcador más alto: {}".format(contador, marcador_alto), align="center", font=("verdana", 15))


    if serpiente.distance(comida) < 20: #nos permite determinar la distancia a un objeto
        x = random.randint(-250, 250);
        y = random.randint(-250,250);
        comida.goto(x,y);

        #nuevo segmento al comer 
        nuevo_cuerpo = turtle.Turtle();
        nuevo_cuerpo.shape("square");
        nuevo_cuerpo.color("green");
        nuevo_cuerpo.penup();
        nuevo_cuerpo.goto(0,0); #posicion inicial
        nuevo_cuerpo.speed(0);

        #agregando a la lista
        cuerpo.append(nuevo_cuerpo);
    
        #aumento de marcador
        contador += 10;
        if contador > marcador_alto:
            marcador_alto = contador;
            texto.clear(); #limpiamos el texto
            #actualiza el marcador
            texto.write("Marcador: {} \t Marcador más alto: {}".format(contador, marcador_alto), align="center", font=("verdana", 15));


    total = len(cuerpo); #medida de la lista
    for i in range(total -1, 0, -1): #inica en el -1 hacia atras, 0= no se cuenta, -1 = la cuenta ira de uno en uno 
        x = cuerpo[i - 1].xcor(); #llamamos a la lista, i = contador y -1 porque empezara a contar en el 0, y devolvera la coordenada en x
        y = cuerpo[i -1].ycor();
        cuerpo[i].goto(x, y); #encviando el cuerpo a la par de la serpiente
        
    if total > 0:
        x = serpiente.xcor(); #devolvera coordenada en x
        y = serpiente.ycor();
        cuerpo[0].goto(x,y); #para luego enviar el cuerpo a dicha coordenada, para que siga la cabeza de la serpiente 


    movimiento();

    #reiniciando el juego cuando se toca el cuerpo
    for i in cuerpo:
        if i.distance(serpiente) < 20: #si i(cada cuerpo) se toca con la serpiente 
            for i in cuerpo: #recorrera toda la lista y eliminara
                i.clear();
                i.hideturtle();
            serpiente.home(); #la serpiente vuelve al 0,0
            serpiente.direction = "stop"; #se queda en stop hasta que presionemos otra tecla 
            cuerpo.clear(); #impiamos la lista 

                


    time.sleep(retraso); #cuando la serpiente se mueva haga un pequeño delete para que no vaya muy rapido 


turtle.done();