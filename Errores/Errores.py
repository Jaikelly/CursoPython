
while True:
    try: #intentar
        edad = int(input("Ingresa tu edad: "));
        print("Tu edad es: ", edad)
        break
    except:
        print("Ingresaste un valor erroneo")
    finally: #se ejecuta siempre
        print("Finalizado")