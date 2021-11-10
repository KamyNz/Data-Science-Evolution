class Persona:

  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad

  def saluda(self,otra_persona):
    #print(f'Esta entrando en saluda')
    return f'Hola {otra_persona.nombre}, me llamo {self.nombre}'

david = Persona('David',35)
erika = Persona('Erika',30)

david.saluda(erika)

# Hay variables privadas, por lo cual se usa una convencion

