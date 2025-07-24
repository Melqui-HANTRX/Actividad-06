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


def triangular(base, altura):
    return (base + altura) / 2


def numerParoInpar(numeropar):
    return "par" if numeropar % 2 == 0 else "impar"


def promedioDecalificaciones():
    n = int(input("Cuantas calificaciones se ingresaran?: "))
    suma = 0
    for i in range(n):
        calificacion = float(input(f"ingrese la calificacion{i + 1}: "))
        suma += calificacion

    promedio = suma / n if n != 0 else 0
    return promedio


def mayorOmenor():
    n = int(input("Cual es la cantidad de numeros a ingresar?: "))
    if n <= 0:
        print("Cantidad invalida.")
        return None, None
    primerNumero = float(input(f"Ingrese el (1) numero: "))
    mayor = menor = primerNumero

    for i in range(1, n):
        num = float(input(f"Ingrese el ({i + 1}) numero: "))
        if num > mayor:
            mayor = num
        if num < menor:
            menor = num
    return mayor, menor


def menu():
    while True:
        print("\n--- MENÚ DE OPERACIONES ---")
        print("1. Ingresar n números: suma, promedio, positivos y negativos")
        print("2. Calcular el área de un triángulo")
        print("3. Verificar si un número es par o impar")
        print("4. Calcular el promedio de n calificaciones")
        print("5. Ingresar números y mostrar el mayor y el menor")
        print("6. Salir del programa\n")

        opcion = input("Seleccione una opcion 1-6: ")

        match opcion:
            case "1":
                suma, prom, pos, neg = ingresar_contar()
                print(f"Suma total: {suma}")
                print(f"Promedio: {prom:.2f}")
                print(f"Cantidad de numeros negativos: {neg}")
                print(f"cantidad de numeros positivos: {pos}")

            case "2":
                base = float(input("Ingrese la base del triangulo: "))
                altura = float(input("Ingrese la altura del triangulo: "))
                area = triangular(base, altura)
                print(f"Area del triangulo: {area:.2f}")
            case "3":
                numero = int(input("Ingrese un numero: "))
                resultado = numerParoInpar(numero)
                print(f"El numero {numero} es {resultado}")
            case "4":
                promedio = promedioDecalificaciones()
                print(f"El promedio de las calificaciones es {promedio:.2f}")
            case "5":
                mayor, menor = mayorOmenor()
                if mayor is not None:
                    print(f"El numero mayor es {mayor:.2f}")
                    print(f"El numero menor es {menor:.2f}")
            case "6":
                print("Gracias por visitarnos, saliendo del programa...")
                break
            case _:
                print("opcion invalida..... redirigiendo.... intente de nuevo")


menu()



