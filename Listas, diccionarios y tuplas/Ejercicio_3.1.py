
paises = {"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Honduras",
"Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama":"Panama", "Argentina": "Buenos Aires",
"Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"};

dato = input("Ingrese pais: ");
letra = dato.capitalize() in paises #pone la primera letra en mayuscula y si esta desntro de paises
print(letra);

if letra == True:
    print(paises[dato.capitalize()]);
else:
    print("tu pais no esta en el diccionario");
