

def totalFactura():
    cantidad = float(input("Ingrese cantidad: "));
    iva = int(input("Ingrese IVA a aplicar: "));
    if iva == 0:
        resultadoIva = cantidad * 0.21;
        resultadoFinal = cantidad + resultadoIva;
        return "El valor final con un 21% es: ", resultadoFinal;
    else:
        resultadoIva = (cantidad * iva) / 100;
        resultadoFinal = cantidad + resultadoIva;
        return "El valor final con un ", iva, "% es: ", resultadoFinal;

print(totalFactura());
