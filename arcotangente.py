import math
def arctan(x, n):
    aproximacion = 0
    for i in range(n):
        aproximacion += ((-1) ** i) * (x ** (2 * i + 1)) / (2 * i + 1)
    return aproximacion
x = float(input("Ingrese el valor de x (debe estar en el rango [-1, 1]): "))
if x < -1 or x > 1:
    print("Pero le acabé de decir que el valor de x debe estar en el rango [-1, 1].")
    print("¿Usted cree que " +str(x)+ " está en el rango [-1, 1]?")
else:
    n = int(input("Ingrese el número de términos de la serie de Maclaurin a utilizar: "))
    aproximacion = arctan(x, n)
    valor_real = math.atan(x)
    diferencia = valor_real - aproximacion
    print("La aproximación de la función arcotangente para x = " +str(x)+ " utilizando los primeros " +str(n)+ " términos de la serie de Maclaurin es: " +str(aproximacion))
    print("El valor real de la función arcotangente para x = " +str(n)+ " es: " +str(valor_real))
    print("La diferencia entre la aproximación y el valor real es: " +str(diferencia))