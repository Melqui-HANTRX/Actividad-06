def ingresar_numeros():
    n = int(input("Cuantos numeros desea agregar?: "))
    numeros = []
    for i in range(n):
        suma = float(input(f"Ingrese el numero: {i+1}"))
        numeros.append(suma)
    return numeros




