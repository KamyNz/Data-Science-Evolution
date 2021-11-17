"""
Notas:
  -Clases de complejidad algoritmica

  -O(1): Constante
  -O(n): Lineal
  -O(log n): Logaritmico
  -O(n log n): Logaritimico lineal
  -O(n**2): Ojo, ese es n a la potencia
  -O(2**n): Ojo, esto es 2 a la N potencia, no a la N potencia.
"""

"""
Notas - Busqueda Lineal:
  -Busca en todos los elementos de forma secuencial

  -Siempre pensar:
    -Cual es el peor caso ?
"""
import random

def busqueda_lineal(lista, objetivo):
  match = False

  for elemento in lista: # O(n), es la complejidad algoritmica
    if elemento != objetivo:
      pass
    else:
      match = True
      break
  return(match)

if __name__ == '__main__':
  size_list = int(input('De que tamano es tu lista? '))
  objective= int(input('Que numero quieres encontrar? '))

  #creating random list
  lista= [random.randint(0,100) for i in range(size_list)]

  #Creando objeto encontrado para uso en print de acuerdo a funcion de arriba
  encontrado = busqueda_lineal(lista, objective)
  print(lista)
  #Se esta usando operadores terniarios en Python ~ para generar un if/else en una sola linea
  print(f'El elemento {objective} {"esta" if encontrado else "no esta"}')
