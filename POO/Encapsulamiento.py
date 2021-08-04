#Declarar atributos solo para una clase, es decir, privado

class A():
    def __init__(self):
        self.contador = 0;

    def  incrementar(self):
        self.contador += 1;

    def cuenta(self):
        return self.contador;

class B():
    def __init__(self):
        self.__contador = 0;

    def  incrementar(self):
        self.__contador += 1;

    def cuenta(self):
        return self.__contador;    

a = A();
a.incrementar();
a.incrementar();
print(a.cuenta());
print(a.contador);

b = B();
b.incrementar();
b.incrementar();
print(b.cuenta());
#print(b.__contador); #devuelve un error ya que esta encapsulado, solo se puede utilizar dentro de la clase
print(b._B__contador); #asi se podria usar el atributo encapsulado
        
        
        