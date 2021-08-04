
class Persona():
    nombre = "Carlos";
    apellido = "Vergara";
    sexo = "Masculino";
    edad = 30;
    
    #Metodos
    def hablar(self,mensaje): #self una variable este en el contexto de una clase
        return mensaje;

#Objeto
persona1 = Persona();

persona1.nombre;
persona1.apellido;
persona1.sexo;
persona1.edad;

print(persona1.hablar("Hola soy"), "{} y mi apelldio es {}, tengo {} y de sexo soy {}".format(persona1.nombre,persona1.apellido,
persona1.edad,persona1.sexo));