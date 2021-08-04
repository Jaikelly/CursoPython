#Listas

lista = ["Tomate", "Cebolla", "Huevos", "Leche", "Arroz"];
lista2 = [1, 2, 3, 4, 5];
lista3 = [6, 7, 8, 9, 10];

print(lista);
print(lista2);
print(lista3);

#en que posicion esta cada datos
print(lista[1]);
print(lista2[4]);
print(lista3[0]);

#el dato esta en la lista?
print("Leche" in lista);

#recorrer listas
print(lista2[0:4]); #del 0 al 4

#unir listas
print(lista2 + lista3);

#modificar lista
lista[0] = "Ajo";
print(lista);
