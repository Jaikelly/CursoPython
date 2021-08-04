
#se ocupa para designar multiples clases padres a una clase hija 

#clases padres
class A():
    def mensaje(self):
        print("Esta en la clase A");
    
    def primera(self):
        print("Estas dentro de la clase A");

class B():
    def mensaje(self):
        print("Esta en la clase B");

    def segundo(self):
        print("Estas dentro de la clase B");

#clase hija
class C(A,B):
    pass;

c = C();
c.primera();
c.segundo();