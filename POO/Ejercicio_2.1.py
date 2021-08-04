
class Calculo():
    def __init__(self):
        self.valor1 = int(input("Ingrese primer valor: "));
        self.valor2 = int(input("Ingrese segundo valor: "));

    def suma(self):
        self.resulSuma = self.valor1 + self.valor2;
        print("El resultado de la suma es: ", self.resulSuma);
    
    def resta(self):
        self.resulResta = self.valor1 - self.valor2;
        print("El resultado de la resta es: ", self.resulResta);

    def multiplicacion(self):
        self.resulMulti = self.valor1 * self.valor2;
        print("El resultado de la multiplicacion es: ", self.resulMulti);

    def division(self):
        self.resulDivi = self.valor1 / self.valor2;
        print("El resultado de la division es: ", self.resulDivi);


calcular = Calculo();
calcular.suma();
calcular.resta();
calcular.multiplicacion();
calcular.division();
        
        