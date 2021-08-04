#poder editar los metodos que una clase padre ya posee

#clase padre
class Animales():
    def __init__(self,nombre,mensaje):
        self.nombre = nombre;
        self.mensaje = mensaje;

    def hablar(self):
        print(self.mensaje);

#clase hija
class Perro(Animales):
    #se modifica el metodo de la clase padre 
    def hablar(self):
        print("Yo hago guau");

#otra clase hija
class Pez(Animales):
    def hablar(self):
        print("Yo no hablo");

perro = Perro("Firulai","Guau");
perro.hablar();

#recorremos en una lista las clases con el metodod hablar 
animalesLista = [Perro("Firulai", "Guau"), Pez("Nemo", "Nada")];
for i in animalesLista:
    print(i.hablar());
