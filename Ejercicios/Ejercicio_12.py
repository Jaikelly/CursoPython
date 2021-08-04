
voto = input("Ingrese la letra del candidato: ");

if voto in "aA":
    print("Usted ha votado por: ", voto.upper(), "Partido rojo");
elif voto in "bB":
    print("Usted ha votado por: ", voto.upper(), "Partido verde");
elif voto in "cC":
    print("Usted ha votado por: ", voto.upper(), "Partido azul");
else:
    print("Opción erronea");

