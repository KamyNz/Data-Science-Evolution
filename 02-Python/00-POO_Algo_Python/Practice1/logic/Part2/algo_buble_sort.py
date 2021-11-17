import random

def buble_sort(lista):
  pass



if __name__ = '__main__':
  size_list = int(input('De que tamano es tu lista? '))
  objective= int(input('Que numero quieres encontrar? '))

  #creating random list
  lista= [random.randint(0,100) for i in range(size_list)]
  print(lista)

  lista_sorted = buble_sort(lista)
  print(lista_sorted)
