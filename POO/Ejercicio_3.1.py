
class Fabrica():
    def __init__(self, llantas, color, precio):
        self.llantas = llantas;
        self.color = color;
        self.precio = precio;

class Carro(Fabrica):
    def datos(self):
        print("La cantidad de llantas es: ", self.llantas);
        print("El color del carro es: ", self.color);
        print("El precio del carro es: $", self.precio);
        

class Moto(Fabrica):
    def datos(self):
        print("La cantidad de llantas es: ", self.llantas);
        print("El color del carro es: ", self.color);
        print("El precio del carro es: $", self.precio);

moto = Moto(2, "Negro", 4000);
moto.datos();

carro = Carro(4, "Blanco", 5000);
carro.datos();