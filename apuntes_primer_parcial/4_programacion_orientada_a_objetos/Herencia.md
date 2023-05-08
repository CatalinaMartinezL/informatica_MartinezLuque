> = → no hay return → modifica el valor
> == → hay return → T o F
> Ejemplo de heredar:
class Ave:
  def __init__(self, energia):
    self.energia = energia
  def volar(self):
    self.energia -= 20

class Condor(Ave):
  def dormir(self,minutos):
   self.energia += minutos * 3
    
    > Condor hereda de ave que self.energia=energia y lo de volar. Condor es un ave.

> <Clase abstracta.
    > Si en la clase abstracta puse algo, se puede *modificar en la subclase*. Redefinir el método. 
    > Ejemplo:
        > En colectivo se eliminó el “maximo_de_personas”
        > Se inicializa el atributo “self.pasajeros”
        > Se inicializa self.combustible con 100.


> <Clase concreta.
    >Proveen comportamiento a sus subclases.
    > Clase madre.
    > Crean instancias
> <Super> → se utiliza en las subclases.
    > Evalúa el método con el mismo nombre de su superclase y además lo que se está redefiniendo. →

