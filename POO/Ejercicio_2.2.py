
class Area():
    def valores(self, base, altura):
        self.base = base;
        self.altura = altura;
    
    def aCuadrado(self):
        self.cuadrado = self.base * self.altura;
        print("El area del cuadrado es: ", self.cuadrado);

    def aTriangulo(self):
        self.triangulo = (self.base * self.altura) / 2;
        print("El area del triangulo es: ", self.triangulo);

    def aPentagono(self, perimetro, apotema):
        self.perimetro = perimetro;
        self.apotema = apotema;
        self.pentagono = (5 * self.perimetro * self.apotema) / 2;
        print("El area del pentagono es: ", self.pentagono);

calculo = Area();
calculo.valores(5,5);
calculo.aCuadrado();
calculo.aTriangulo();
calculo.aPentagono(4,4);

        
