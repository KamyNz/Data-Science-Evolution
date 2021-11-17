class Auto():

  # Properties of auto => model, brand, color
  def __init__(model, brand, color):
      self.model = model
      self.brand = brand
      self.color = color

      self._state = 'stop' #Private property
      self._motor = Motor(cilinders=4) #Private property, when I want to get by defautl with Motor

  def put_speed(self, type='slow'):
    # step1: Putting speed to know change of state
    if type == 'fast':
      self._motor.put_speed(10)
    else:
      self._motor.put_speed(3)

    # step2: Changing state
    self._state = 'moving'


class Motor():

  def __init__(self, cilinders, type='gasoline'):
    self.cilinder = cilinders
    self.type = type
    self_temperatura = 0

  def get_gasoline(self, quantity):
    pass





