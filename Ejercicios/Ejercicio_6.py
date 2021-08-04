#promedio

p1 = float(input("Ingrese nota de primera practica: "));
p2 = float(input("Ingrese nota de segunda practica: "));
p3 = float(input("Ingrese nota de tercera practica: "));
ep = float(input("Ingrese nota del Examen Parcial: "));
ef = float(input("Ingrese nota del Examen Final: "));

promPractica = (p1 + p2 + p3) / 3;
promFinal = (promPractica + ep + ef) / 3;

print(promFinal);