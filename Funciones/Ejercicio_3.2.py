
def numeros(*valores):
    lista = [];
    resultado = 0;
    for i in valores:
        lista.append(i);
        resultado = i + resultado;
    print(lista);
    resultado = resultado / len(lista)
    return resultado;

print(numeros(4,5,7,3,4,4));