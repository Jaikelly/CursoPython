#primera forma
numeros = [1,2,3,4,5,6,7,8,9,10];
print(numeros);

#segunda forma
for i in range(1, 11): #rango, imprimera hasta el 10
    print(i);

num1 = int(input("Ingrese un numero: "));
num2 = int(input("Ingrese otro numero: "));

for i in range(num1, num2 + 1):
    print(i);