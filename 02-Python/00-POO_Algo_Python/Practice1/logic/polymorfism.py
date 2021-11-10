"""
Se puede usar el concepto (Jerarquias para modelar) de Superclase y esta comparte
comportamiento con una subclase.

Notas: Polimorfismo

  -La habilidad de tomar varias formas
  Eje:
    -Vehiculo (Tren, avion, automovil) <= Se desplazan de forma distinta

  -En Python, nos permite cambiar el comportamiento de una superclase para adaptarlo
  a la subclase.
    -Using Overwriting.

  -Conclusion: Se puede tomar metodo de Superclase y cambiar su comportamiento de implementacion en
  la subclase
"""

# Superclase Persona
class Persona:

  def __init__(self,nombre,):
    self.nombre = nombre

  def avanza(self):
    print(f'{self.nombre} esta caminando')


# Subclase ciclista, esta esta extendiendo de la superclase Persona
class Ciclista(Persona):

  def __init__(self, nombre):
      super().__init__(nombre)

  def avanza(self):
      print(f'{self.nombre} esta moviendose en su bicicleta')

# Creating main
def main():
  persona = Persona('Camila')
  persona.avanza()

  ciclista = Ciclista('Daniel')
  ciclista.avanza()

# Executing main
if __name__ == '__main__':
  main() #calling main

