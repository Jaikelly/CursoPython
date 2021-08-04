#llave y valor
diccionario = {1: "Manuel Garcia", 2: "Andrea", 3: "Jaikelly Mota"};

print(type(diccionario));
print(diccionario);

#devuelve el valor de la llave 3
print(diccionario[3]);

#esta o no?
print(2 in diccionario);

#no conozco la clave 
value = diccionario.values(); #lo pasamos a una lista 
print("Manuel Garcia" in value);