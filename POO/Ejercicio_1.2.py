
class Calculo():
    def datos(self, x, n):
        self.x = x;
        self.n = n;

    def calculo(self):
        self.resultado = pow(self.x, self.n);
        print("El resultado de base {} y exponente {} es: {}".format(self.x, self.n, self.resultado));
        
ejercicio1 = Calculo();
ejercicio1.datos(3,4);

ejercicio1.calculo();