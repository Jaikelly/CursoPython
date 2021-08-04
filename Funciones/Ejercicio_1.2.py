

def numero():
    num = int(input("Ingrese un numero: "));
    if num < 0:
        print("Debe ser un numero positivo");
    else:
        resultado = 1;
        i = 1;
        while i <= num:
            resultado = resultado * i; 
            i = i + 1; 
            print(resultado);


numero();
    