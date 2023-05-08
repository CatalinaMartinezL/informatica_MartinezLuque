> Se puede usar self y append juntos. Ej:
  class Biblioteca:
    def __init__(self):
      self.libros = []
    def agregar_libro(self, libro):
      self.libros.append(libro)
> Listas por comprensión → permite hacer mapeos y filtrados de la lista.

# SETS
> Parecidos a las listas.
> No tienen elementos repetidos.
> Sus elementos no están ordenados.

# TUPLA
> Retornar más de una cosa y sabemos exactamente cuantas.
> Ej: que me devuelva las primeras letras del nombre, segundo y apellido.
  class Persona:
    def __init__(self, un_nombre, un_segundo_nombre, un_apellido):
      self.nombre = un_nombre
      self.segundo_nombre = un_segundo_nombre
      self.apellido = un_apellido
    
    def iniciales(self):
      return (self.nombre[0], self.segundo_nombre[0], self.apellido[0])

    > Estoy pidiendo la posición 0. 
> También se puede usar + - * /
  > ej: 
  def precios_con_iva (self):
    return self.precio_minorista * 1.21, self.precio_mayorista *1.21



