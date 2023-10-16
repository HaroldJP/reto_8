import math
def maclaurin(x, n):
    aproximacion = 0
    for i in range(n):
        aproximacion += (x ** i) / math.factorial(i)
    return aproximacion
x = float(input("Ingrese el valor de x: "))
n = int(input("Ingrese el número de términos de la serie de Maclaurin a utilizar: "))
aproximacion = maclaurin(x, n)
valor_real = math.exp(x)
diferencia = valor_real - aproximacion
print("La aproximación de la función exponencial para x = " +str(x)+ " utilizando los primeros " +str(n)+ " términos de la serie de Maclaurin es: " +str(aproximacion))
print("El valor real de la función exponencial para x = " +str(x)+ " es: " +str(valor_real))
print("La diferencia entre la aproximación y el valor real es: " +str(diferencia))