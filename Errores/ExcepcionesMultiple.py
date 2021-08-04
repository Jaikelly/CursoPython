
while True:
    try:
        num1 = int(input("Ingresa un numero: "));
        resultado = 100 / num1;
        print(resultado);
        break;
    except ZeroDivisionError:
        print("No se puede dividir entre cero");

while True:
    try:
        edad = int(input("Ingresa tu edad: "));
        print("Tu edad es: ", edad);
        break;
    except ValueError: #me evaluara si es un string o float, etc
        print("Has colocado un valor erroneo");

while True:
    try:
        edad = int(input("Ingresa tu edad: "));
        print("Tu edad es: ", edad);
        break;
    except KeyboardInterrupt: #control c, se finaliza la ejecucion 
        print("\nHas cancelado la ejecucion");
        break;
