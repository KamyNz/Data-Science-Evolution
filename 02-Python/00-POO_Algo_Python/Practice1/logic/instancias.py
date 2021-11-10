from typing import Coroutine


class Coordenada():

  #Generating constructor
  def __init__(self,x,y):
      self.x = x
      self.y = y

  #Creating distance method
  def distancia(self, otra_coordenada):
    x_diff = (self.x - otra_coordenada.x)**2
    y_diff = (self.y - otra_coordenada.y)

    return (x_diff + y_diff)**0.5

# Using main method
if __name__ == '__main__':
  coord_1 = Coordenada(3,30)
  coord_2 = Coordenada(4,9)

  print(coord_1.distancia(coord_2))

  #using isistance to give false
  print(f'Using isistance to give false')
  print(isinstance(4,Coordenada))

  #using isistance to give true
  print(f'Using isistance to give true')
  print(isinstance(coord_1,Coordenada))


