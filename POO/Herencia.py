class Animales():
    def __init__(self,descripcion,especie,hablar):
        self.descripcion = descripcion;
        self.especie = especie;
        self.hablar = hablar;

    def habla(self):
        print("Yo hago: ", self.hablar);

    def  describir(self):
        print("Soy de la especie: ", self.especie);


#herada todo de la clase animales 
class Perro(Animales):
    pass

class Abeja(Animales):
    def sonido(self,sonido):
        self.sonido = sonido;
        print(self.sonido);

#objeto
perro = Perro("Perro", "Mamifero", "Guau");

perro.habla(); #llamamamos al metodo habla
perro.describir(); #llamamos al metodo describir

#objeto
abeja = Abeja("Abeja", "Insecto", "Brr"); 
abeja.sonido("Brr"); #llamamos al metodo sonido de la clase abeja 
abeja.describir(); #llamamos al metodo describir que herada de la clase animales