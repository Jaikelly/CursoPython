
palabra1 = input("Ingrese su primera palabra: ");
palabra2 = input("Ingrese su segunda palabra: ");

if len(palabra1) < 3 or len(palabra2) < 3: #len cuenta los caracteres 
    print("No, riman porque alguna de ellas tiene menos de 3 caracteres");
elif palabra1[-3:] == palabra2[-3:]: #ultimos 3 caracteres son iguales 
    print("Las palabras riman");
elif palabra1[-2:] == palabra2[-2:]: #ultimos dos caracteres 
    print("Las palabras riman un poco");
else:
    print("No riman");