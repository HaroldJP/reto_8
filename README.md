# reto_8
### Punto 1

Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.

```python
for i in range(1, 101):
    print(i, i**2)
```

### Punto 2

Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.

```python
print("Números impares:")
for i in range(1, 1000, 2):
    print(i)
print("Números pares:")
for j in range (2, 1001, 2):
    print(j)
```

### Punto 3


Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado

```python
n  = int(input("Ingrese un número natural mayor o igual a 2: "))
print("Los números pares en forma descendente desde " +str(n)+ " hasta 2 son:")
if n % 2 != 0:
    n = n - 1
else:
    n = n
for i in range(n, 1, -2):
    print(str(i))
```

### Punto 4

Imprimir los números de 1 hasta un número natural n dado, cada uno con su respectivo factorial

```python
import math
n = int(input("Ingrese un número natural: "))
for i in range(1, n+1):
    print(i, math.factorial(i))
```

### Punto 5

Calcular el valor de 2 elevado a la potencia n usando ciclos for.

```python
n = int(input("Ingrese un número: "))
m = 1
for i in range(n):
    m *= 2
print(" 2^" +str(n)+ " es igual a " +str(m))
```

### Punto 6

Leer un número natural n, leer otro dato de tipo real x y calcular x^n usando ciclos for. Disclaimer: Trate de no utilizar el operador de potencia (**).

```python
def potencia(n:float, x:int):
  a : int = 1
  for i in range(1,n+1):
    a *= x
  print(str(x)+ "^" +str(n)+ "=" +str(a))
n = int(input("Ingrese un numero natural: "))
x = float(input("Ingrese un numero real: "))
potencia(n,x)
```

### Punto 7

Diseñe un programa que muestre las tablas de multiplicar del 1 al 9.

```python
def tablas(a : int):
    print("La tabla del " +str(a)+ " es:")
    for i in range(1, 11):
        b = a*i
        print(str(n)+ "x" +str(i)+ " = " +str(b))
for n in range(1, 11):
    tablas(n)
```

### Punto 8

Diseñar una función que permita calcular una aproximación de la función exponencial alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función exponencial y mostrar la diferencia entre el valor real y la aproximación.

```python
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
```

### Punto 9

Diseñar una función que permita calcular una aproximación de la función seno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función seno y mostrar la diferencia entre el valor real y la aproximación.

```python
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
```

### Punto 10

Diseñar una función que permita calcular una aproximación de la función arcotangente alrededor de 0 para cualquier valor x en el rango [-1, 1], utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función arctan y mostrar la diferencia entre el valor real y la aproximación.

```python
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
```





