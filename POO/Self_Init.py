
class Persona():
    nombre = False;

    def __init__(self, nombre, apellido): #primer metodo que se va a ejecutar en toda la clase
        self.nombre = nombre;
        self.apellido = apellido;
        print("Has creado el objeto persona. Con el nombre {}".format(nombre));

    def datos(self): #engloba las variables para que sea en toda la clase
        self.nombre = True;

persona = Persona("Juan", "Mota");
persona.datos(); #llamamos al metodo 
print(persona.nombre);