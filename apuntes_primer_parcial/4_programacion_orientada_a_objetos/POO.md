<def>: Entidad computacional que me permite interactuar.

# CARACTERISTICAS
> Me puedo comunicar, entiende mensajes, tiene referencias internas y es consciente de eso.
> Pueden tener distintos estados basales.
> Aunque haya distintos estados basales, los objetos pueden entender los mismos métodos (métodos == mensaje)
> Pueden entender los mismos mensajes aunque sean de otra clase.
> Objeto dentro de una clase → instancia.
> Conjunto de mensajes/métodos que entiende la clase → interfaz
> Las distintas clases tienen interfaces parecidas
> Objetos que comparten interfaz y hay una tercer clase que los usa→ polimórficos
> Puede ser parcial o total.
> Ellos no saben que son polimórficos. Se necesita de un observador/otro actor para verlo.
  >Estado → se da por el conjunto de atributos
> Puede cambiar o modificarse con el tiempo. Por ejemplo luego de dar órdenes (comer, volar, etc.)
> <Raise Exception(“”): 
>

# DICCIONARIO
> *Clase*: class <Clase>
> *Atributo*:   def __init__ (self, parametro, parametro) 
    > el atributo es: <self.atributo>
> *Método*: def <metodo> (self, parámetros(o no)): sería como la función
	return o self. o self
> *Estado*: conjunto de atributos.
> *Metodos* == mensajes
> *Instancia*: objeto dentro de clase.
> *Interfaz*: Conjunto de mensajes/métodos que entiende la clase
> *Polimorfismo*: Objetos que comparten interfaz y hay una tercer clase que los usa

# Se pueden usar funciones que ya conocemos...
> str.startswith, str.endswith, str.strip, str.lower, list.remove, .upper
> En vez de list.append(numeros, 32);
    > numeros.append(32)
    > Donde numeros es el objeto, append la función y 32 el nro que quiero agregar.

