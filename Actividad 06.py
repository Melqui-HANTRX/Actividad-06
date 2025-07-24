def Ingrese_numeros():
    numeros = input("Que cantidad de numeros desea agregar5?:" )
    numeropositivo = 0
    numeronegativo = 0
    for  i in  range(numeros):
        sum = input(f"Ingrese el numero{i+1}")
        sum += numeros
        if sum > 0:
            numeropositivo +=1
        if sum < 0:
             numeronegativo +=1}

