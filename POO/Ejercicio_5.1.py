
class Universidad():
    def __init__(self, nombreUni):
        self.nombreUni = nombreUni;

class Carrera():
    def carrera(self, especialidad):
        self.especialidad = especialidad;

class Estudiante(Universidad,Carrera):
    def datos(self, nombre, edad):
        self.nombre = nombre;
        self.edad = edad;
        print("Mi nombre es {}, tengo {} años, mi especialidad es {}, estudio en la Universidad {}".format(self.nombre,
        self.edad, self.especialidad, self.nombreUni));

persona = Estudiante("IEP");
persona.carrera("Programador");
persona.datos("Jaikelly", 20);