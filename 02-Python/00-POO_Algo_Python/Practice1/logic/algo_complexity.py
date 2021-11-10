"""
Notas: Algorithm Complexity
  - Por que queremos pensar en complejidad algoritmica ?
  R//

  - Complejidad temporal vs Complejidad Espacial
  R// Temporal (El tiempo que tarda en ejecutarse),
  Espacio (El espacio en memoria que puede tomar)

  - Podemos definirla como T(n)
  R// funcion t, que recibe un input n

Se debe tener en cuenta aproximacion T(n):
  -Cronometrar tiempo en que corre un algoritmo
  -Contar los pasos con medida abstractar de operacion
  -Contar los pasos conforme nos aproximamos al infinito
    R// Esta tiene en cuenta medida asintotica.

"""

"""
Aproximacion por tiempo, pero esto va a depender de los recursos del dispositivo
en los que se ejecute el algoritmo.
"""
import time

def factorial(n):
  respuesta = 1

  while n > 1:
    respuesta = respuesta * n
    n -= 1
    return(respuesta)

# Factorial recursivo, y se debe poner distintos casos
def factorial_r(n):
  # Caso base: n = 1
  if n == 1:
    return 1

  return(n * factorial(n - 1))

if __name__ == "__main__":
  n = 1000

  # Complejidad temporal caso 1
  comienzo = time.time()
  print(factorial(n))
  final = time.time()
  print(f"Tiempo de ejecucion con caso 1: {final - comienzo}")

  # Complejidad temporal caso 2
  comienzo = time.time()
  print(factorial_r(n))
  final = time.time()
  print(f"Tiempo de ejecucion con caso 2: {final - comienzo}")

  # n = int(input("Ingrese un numero: "))
  # tiempo_inicial = time.time()


"""
Aproximacion por conteo de pasos dado una expresion matematica

Que puede pasar:
  -Cuando tenemos constante:
  -Cuando tenemos terminos cuadrados:

"""
def f(x):
  respuesta = 0

  for i in range(1000):
    respuesta += 1

  for i in range(x):
    respuesta += x

  for i in range(x):
    print(i)

  for i in range(x * x):
    print(i)

  for i in range(x):
    for j in range(x):
      print(i,j)

  return(respuesta)

# From image
#Rojo=función polinómica
#Azul = función lineal
#Amarillo = Función Logarítmica
#Verde = Constante.

"""
Notacion asintotica o Big(O(n)):

Crecimiento asintotico (Conforme se va al infinito):
  -No importan variaciones pequeñas

  -Se centra en lo que pasa conforme el tamaño del problema se acerca al infinito

  -Benchmarking se puede dar:
    -Peor de los casos (Esta es la medida que mejor permite comparar los algoritmos)
    -Mejor de los casos
    -Promedio


  -Big O

  -Solo importa el termino de mayor tamaño

"""
def f(x):
  respuesta = 0

  for i in range(1000):
    respuesta += 1
#O(x) + O(x) = O(x+x) = O(2x) = O(x) //Crecimiento lineal
  for i in range(x):
    respuesta += x

###############################################################################
#O(x) + O(x*x) = O(x*x) = O(n + n^2) = O(n^2) //Crecimiento exponencial
  for i in range(x):
    print(i)

  for i in range(x * x):
    print(i)

###############################################################################

#O(x) O(x) = O(xx) = O(x^2) //Crecimiento exponencial
  for i in range(x):
    for j in range(x):
      print(i,j)

  return(respuesta)

"""
Algoritmo de Fibonnaci recursivo
"""

def fibonacci(n):

  if(n == 0 or n == 1):
    return 1

  return fibonacci(n-1) + fibonacci(n-2) # Dado que se esta llamando 2 veces la funcion, y estas son llamadas recursividad

#2 O(n) O(n) = O(n * n) = O(2**n)  //tiene varias llamadas recursivas y eso hace al algoritmo con un crecimiento exponencial

