
def suma(a,b): #argumentos
    return a + b;

print(suma(2,3)); #le ponemos valor a los argumentos

def resta(num1 = None, num2 = None):
    if num1 == None:
        print("No has ingresado los valores");
        return ;
    return num1 - num2;

print(resta(num1 = 1, num2 = 2));
print(resta(34, 14));