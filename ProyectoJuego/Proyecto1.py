import turtle;
from turtle import  *;
import random; 


s = turtle.Screen();
s.title("Proyecto 1");

class Gamer():

    def juego(self):
        #jugadores
        jugador1 = turtle.Turtle();
        jugador2 = turtle.Turtle();

        #cambiando forma y color
        jugador1.hideturtle();
        jugador1.shape("turtle");
        jugador1.color("green", "green");
        jugador1.shapesize(2,2,2);
        jugador1.pensize(3);

        jugador2.hideturtle();
        jugador2.shape("turtle");
        jugador2.color("red", "red");
        jugador2.shapesize(2,2,2);
        jugador2.pensize(3);

        #creando el circulo del jugador 1 
        jugador1.penup();
        jugador1.goto(200, 90);
        jugador1.pendown();
        jugador1.circle(40);

        #llevandola al principio
        jugador1.penup();
        jugador1.goto(-200, 125);
        jugador1.showturtle();

        #creando el circulo del jugador 2
        jugador2.penup();
        jugador2.goto(200, -110);
        jugador2.pendown();
        jugador2.circle(40);

        #llevandola tortuga al principio sin que se vea 
        jugador2.penup();
        jugador2.goto(-200, -75);
        jugador2.showturtle();

   
        #creacion del dado
        dado = [1,2,3,4,5,6];

        #utilizando el metodo pos
        for i in range(20): #20 hace referencia a los pasos de la tortuga a llegar a la meta 
            if jugador1.pos() >= (200,90):
                ##print("La tortuga verde ha ganado");
                hideturtle();
                write("La tortuga verde ha ganado", ("arial", 20, "bold italic"))
                break;
            elif jugador2.pos() >= (200, -110):
                #print("La tortuga roja ha ganado");
                hideturtle();
                write("La tortuga roja ha ganado", ("arial", 20, "bold italic"));
                break;
            else:
                #turno del jugador 1
                turno1 = input("TURNO JUGADOR VERDE \nPresiona la tecla enter para avanzar");
                turno1 = random.choice(dado); #tomara un numero aleatoria
                print("Tu numero es: ", turno1, "\n Avanzas:", turno1 * 20);
                jugador1.pendown();
                jugador1.forward(20 * turno1);

                #turno del jugador 2
                turno2 = input("TURNO JUGADOR ROJO \nPresiona la tecla enter para avanzar");
                turno2 = random.choice(dado); #tomara un numero aleatoria
                print("Tu numero es: ", turno2, "\n Avanzas:", turno2 * 20);
                jugador2.pendown();
                jugador2.forward(20 * turno2);
        #s.clear()



jugar = Gamer()
jugar.juego();


while True:
    volverJugar = textinput("Ha finalizado el juego", "¿Quieres volver a jugar?")
 
    if not volverJugar or volverJugar in "noNoNO":
        s.clear(); #limipia la pantalla 
        hideturtle();
        write("Vuelve pronto!", ("arial", 20, "bold italic"))
        break;
    elif volverJugar in "siSiSI":
        s.clear();
        hideturtle(); #quita la pluma
        jugar.juego()
    else:
        s.clear();
        hideturtle();
        write("Juego finalizado", ("arial", 20, "bold italic")); #mustra el mensaje en la grafica 
 
turtle.done();