
def entero():
    return 12345;

def decimal():
    return 40.6789;

def frase():
    return "Hola";

print(entero());
print(decimal());
print(frase());

def valores():
    return 1,2,3,4,5,6; #nos retorna una tupla

a,b,c,d,e,f = valores(); #cada letra toma un valor
print(a);
print(d);