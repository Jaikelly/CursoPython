
class Alumno():
    def datos(self,nombre,nota):
        self.nota = nota;
        self.nombre = nombre;

    def imprimir(self):
        print("Tu nombre: ", self.nombre)
        print("Nota: ", self.nota)

    def resultado(self):
        if self.nota < 4:
            print("Has reprobado");
        else:
            print("Has reprobado");
            
alumno1 = Alumno();
alumno1.datos("Carlos", 4.5);

alumno2 = Alumno();
alumno2.datos("Michel", 6);

alumno1.imprimir();
alumno1.resultado();

alumno2.imprimir();
alumno2.resultado();