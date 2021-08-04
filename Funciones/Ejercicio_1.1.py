
lista = []; #lista donde se agegaran los numeros que el usuario ingreso
num = 0;

def pedir():
    i = 0;
    while i < 5: #pediremos 5 numeros
        num = int(input("Ingrese un numero: "));
        lista.append(num); #agregar a la lista
        i +=1;


def numeros():
    lista.sort(); #ordenar de menor a mayor
    pares = [];
    impar = [];
    for i in lista:
        if i%2 == 0: #si el recsiduo es 0, el numero es par
            pares.append(i);
        else: #si el residuo no es 0, es impar
            impar.append(i);
    print("Los numeros pares son: {}".format(pares));
    print("Lso numeros impares son: {}".format(impar));

pedir();
print("los numeros ingresados son: {}".format(lista));
numeros();