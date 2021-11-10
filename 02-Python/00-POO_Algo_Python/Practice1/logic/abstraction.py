class Lavadora:

  def __init__(self):
    pass

  # ayudar a definir el ciclo del lavado
  def lavar(self, temperatura='caliente'):

    #metodos internos de clase
    self._llenar_tanque_agua(temperatura)
    self._anadir_jabon()
    self._lavar()
    self._centrifugar()

  def _llenar_tanque_agua(self, temperatura):
    print(f'LLenando tanque con agua con T {temperatura}')

  def _anadir_jabon(self):
    print('Agregando jabon')

  def _lavar(self):
    print('Lavando')

  def _centrifugar(self):
    print('Centrifugando')

if __name__ == '__main__':
  lavadora = Lavadora()
  lavadora.lavar()




