
def numeros():
    num1 = int(input("Ingrese primer numero: "));
    num2 = int(input("Ingrese segundo numero: "));
    if num1 > num2:
        return 1;
    elif num2 > num1:
        return -1;
    else:
        return 0;

print(numeros());