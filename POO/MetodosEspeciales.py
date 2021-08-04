
class Persona():
    #constructor, se crea el objeto
    def __init__(self, nombre, apellido):
        self.nombre = nombre;
        self.apellido = apellido;
        print("El objeto {} {} ha sido creado".format(self.nombre, self.apellido));

    #convierte a cadena de texto
    def __str__(self):
        return "El objeto tiene como atributo el nombre {} y el apellido {}".format(self.nombre, self.apellido)


    #destructor, quita el objeto y lo reemplaza por otro 
    def __del__(self):
        print("El objeto {} {} ha sido destruido".format(self.nombre,self.apellido));
        

persona = Persona("Jaikelly", "Mota");
print(str(persona));
        