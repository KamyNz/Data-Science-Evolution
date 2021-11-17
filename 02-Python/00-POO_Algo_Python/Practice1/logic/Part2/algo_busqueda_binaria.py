"""
Notas - Busqueda Binaria
  -Divide y conquista
  -El problema se divide en 2 en cada iteracion

  -Ojo:
    -Este algoritmo asume que la lista esta ordenada

  -Tiene sentido que:
    -Si se va a buscar 1 sola vez la lista, se puede busqueda lineal
    -Sin embargo, si se va a buscar muchas veces, mejor primero ordenar la lista
    -Trade-Off (Tiempo vs Espacio):
      -Mayor memoria, menos tiempo
      -Mayor tiempo, menos memoria

  -Cual es el peor caso ?:


Notas - Before:
  -Clases de complejidad algoritmica

  -O(1): Constante
  -O(n): Lineal
  -O(log n): Logaritmico
  -O(n log n): Logaritimico lineal
  -O(n**2): Ojo, ese es n a la potencia
  -O(2**n): Ojo, esto es 2 a la N potencia, no a la N potencia.
"""

"""
-Para entender como corre forma iterativa, es importante entender:
  -Los task frames
    -Cada vez que se ejecuta una funcion, se crea un task frame
    -Se ejecuta las mismas condiciones sobre este.
"""
import random


def busqueda_binaria(lista,begin,end,objective):

  print(f'Buscando el {objective} entre {lista[begin]} y {lista[end-1]}') #Ojo: con error de off by one, dado indice y tamano list

  # Caso base 1: Si indice de comienzo esta mas grande que end, no se encontrara elemento en lista
  if begin > end:
    return False

  # Dado que trata de dividir, se puede usar un punto medio
  idx_medio = (begin + end) // 2

  if lista[idx_medio] == objective: # caso exacto donde se encuentre el objective en la mitad de la lista
    return True
  elif lista[idx_medio] < objective: # caso exacto donde se encuentre en la parte de derecha de la lista
    return busqueda_binaria(lista, idx_medio + 1, end, objective) # Este rango (idx_medio + 1, end)=> es parte derecha de lista
  else:
    return busqueda_binaria(lista, begin, idx_medio -1, objective) # Este rango (begin, idx_medio - 1)=> es parte derecha de lista


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
  lista_unsorted= [random.randint(0,100) for i in range(size_list)]
  lista_sorted = sorted(lista_unsorted)

  #Creando objeto encontrado para uso en print de acuerdo a funcion de arriba
  encontrado1 = busqueda_lineal(lista_unsorted, objective)
  encontrado2 = busqueda_binaria(lista_sorted,0,len(lista_sorted),objective) # Parametros para ejecucion entre rango (0, len(lista_sorted))

  print(lista_unsorted)
  print(lista_sorted)
  #Se esta usando operadores terniarios en Python ~ para generar un if/else en una sola linea
  print(f'Con B Lineal: El elemento {objective} {"esta" if encontrado1 else "no esta"}')
  #Se esta usando operadores terniarios en Python ~ para generar un if/else en una sola linea
  print(f'Con B Binaria: El elemento {objective} {"esta" if encontrado2 else "no esta"}')

"""
-Se aconseja los siguientes pasos:
  -Paso 1: Crear el signature
  -Paso 2: Luego pasar a desarrollar desde arriba.
"""
