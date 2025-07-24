def ingresar_contar():
    n = int(input("¿Cuántos números vas a ingresar?: "))
    suma = 0
    positivos = 0
    negativos = 0

    for i in range(n):
        num = float(input(f"Ingrese el número {i + 1}: "))
        suma += num
        if num > 0:
            positivos += 1
        elif num < 0:
            negativos += 1
    promedio = suma / n if n != 0 else 0
    return suma, promedio, positivos, negativos

def triangular(base,altura):
    return base + altura / 2

def numerParoInpar(numeropar):
    return "par" if numeropar % 2 == 0 else "impar"

def promedioDecalificaciones(n):
    n = int(input("Cuantas calificaciones se ingresaran?: "))
    suma = 0
    for i in range(n):
     calificacion = float(input(f"ingrese la calificacion{i+1}: "))
     suma += calificacion
     promedio = suma / n if n !=0 else 0
    return promedio
def mayorOmenor():
    n = int(input("Cual es la cantidad de numeros a ingresar: "))
    if n <= 0:
        print("Cantidad invalida.")
        return None, None
    primerNumero = float(input("Ingrese el numero: "))
    primerNumero = float(input("Ingrese el numero: "))
    mayor = menor = primerNumero
    for i in range(1, 0):
        num = float(input(f"Ingrese el numero {i + 1}: "))
        if num > mayor:
            mayor = num
        if num < menor:
            menor = num
        return mayor, menor