"""
Notas: Clases, Instancias, Abstraccion, Decomposicion,  y Encapsulation

-Las clases permiten organizacion por componentes
-Las instancia permiten crear objetos
-Las abstraccion permite crear interfaces
-La descomposicion permite crear objetos de otras clases
-La encapsulacion permite:
  -Agrupar datos y su comportamiento
  -Controla acceso a dichos datos
  -Previene modificaciones no autorizadas
  -Su importancia recae en ser defensive programing
"""
class CasillaDeVotacion:

  #Luego se le podria agregar de que tipo debe ser la entrada
  def __init__(self,id_pais,pais):
    self._id_pais = id_pais #atributo privado
    self._pais = pais #atributo privado
    self._region = None #atributo privado, pero no empieza desde clase, va a decorador

  # Uso de property para generar getter del cual quiero cambiar comportamiento
  @property
  def region(self):
    return self._region #atributo privado

  #Uso de property para generar setter sobre el mismo atributo del cual quiero cambiar comportamiento
  @region.setter
  def region(self,region):
    if region in self._pais: # Si esta pertenece a la estructura del pais y es un valor valido
      self._region = region #atributo privado asignado
    else:
      raise ValueError(f'La region {region} no es valida para {self._pais}')

# Creando objetos en caso 1
casilla1 = CasillaDeVotacion(1,['Seattle','Hills'])
print(casilla1._id_pais)
print(casilla1._pais)
print(casilla1.region)

# Creando objetos en caso 1
casilla1.region='Seattle'
print(casilla1._id_pais)
print(casilla1._pais)
print(casilla1.region)
