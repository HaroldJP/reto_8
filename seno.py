import math
def seno(x, n):
    aproximacion = 0
    for i in range(n):
        aproximacion += ((-1) ** i) * (x ** (2 * i + 1)) / math.factorial(2 * i + 1)
    return aproximacion
x = float(input("Ingrese el valor de x: "))
n = int(input("Ingrese el número de términos de la serie de maclaurin a utilizar: "))
aproximacion = seno(x, n)
valor_real = math.sin(x)
diferencia = valor_real - aproximacion
print("La aproximación de la función seno para x = " +str(x)+ " utilizando los primeros " +str(n)+ " términos de la serie de maclaurin: " +str(aproximacion))
print("El valor real de la función seno para x = " +str(x)+ " es: " +str(valor_real))
print("La diferencia entre la aproximación y el valor real es: " +str(diferencia))