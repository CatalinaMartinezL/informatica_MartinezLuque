# Identifica la interfaz y el estado de la misma:
class Perro:
    def __init__(self):
        self._alimento = 0
        self._caricias = 0

    def energia(self):
        return self._alimento + (self._caricias * 10)

    def comer(self, gramos):
        self._alimento += gramos

    def acariciar(self):
        self._caricias += 1

    def estaDebil(self):
        return self._caricias < 2

# La interfaz que comparten es la energía, el comer, el acariciar y el estar débil
# Y su estado es self.alimento y self.caricias
    
#Ejercicio 2
# Modificá el método volar de la clase Golondrina visto en la clase de teoría de 
# manera que no pueda volar si al hacerlo la energía toma el valor 0 o valor negativo.


# Ejercicio 3
# Creá una clase Notebook cuyo estado sea: marca, modelo y precio, y que tenga un método
# que le aplique un descuento al precio, el cual tiene que recibir un número entero 
# (el porcentaje de descuento) y tiene que devolver cuánto valdría esa notebook si se aplicase el descuento. 
# Por último hay que instanciar esta clase y en algunos casos aplicar este descuento.

class Notebook:
    def __init__(self, una_marca, un_modelo, un_precio):
        self.marca = una_marca
        self.modelo = un_modelo
        self.precio = un_precio

    def con_descuento(self, descuento):
        self.precio -= (self.precio*(descuento/100))
    
Compu_cata = Notebook("Lenovo", "Yoga", 50000)
Compu_cata.con_descuento(15)
print(Compu_cata.precio)

# Ejercicio 4
# Definí una clase que modele un contador, el cual puede incrementar o disminuir en uno el valor que se ingresa, 
# recordando el valor actual. También puede resetear este valor y al hacerlo se pone en cero. 
# Además es posible indicar directamente un número nuevo que reemplace al valor actual. 
# Este objeto debe entender los siguientes mensajes:
    # inc()
    # dis()
    # reset()
    # valorActual()
    # valorNuevo(nuevoValor)
# Como ejemplo el resultado de ejecutar las siguientes líneas tiene que ser 12 y 25.

class Contador:
    def __init___(self, contador_inicial):
        self.contador = contador_inicial
        contador_inicial = 0
    
    def inc(self):
        self.contador += 1
    
    def dis(self):
        self.contador -= 1
    
    def reset(self):
        self.contador = 0
    
    def valorActual(self):
        return self.contador
    
    def valorNuevo(self, nuevoValor):
        self.valor = nuevoValor


contador = Contador(10)
contador.inc()
contador.inc()
contador.dis()
contador.inc()
contador.valorActual()
contador.valorNuevo(27)
contador.dis()
contador.dis()
contador.valorActual()

# Ejercicio 5
# Modificá el ejercicio anterior de manera que sea capaz de recordar cual fue el último comando
# que se le dió, en forma de mensaje. Estos mensajes pueden ser: "reset", "incremento", "disminución" 
# o "actualización" (para cuando se coloca un valor nuevo). El método para saber el último comando es ultimoComando,
#  y el resultado de aplicarlo a la serie de comandos dicha en el ejercicio anterior debería ser "disminución".

class Contador:
    def __init___(self, contador_inicial):
        self.contador = contador_inicial
        contador_inicial = 0
        self.ultimo_comando = None

    def inc(self):
        self.contador += 1
        self.ultimo_comando = "incremento" 
    
    def dis(self):
        self.contador -= 1
        self.ultimo_comando = "disminución"
    
    def reset(self):
        self.contador = 0
        self.ultimo_comando = "reset"
    
    def valorActual(self):
        return self.contador
    
    
    def valorNuevo(self, nuevoValor):
        self.valor = nuevoValor
        self.ultimo_comando = "Actualizado"

    def ultimo_comando(self):
        return self.ultimo_comando 
    

# Ejercicio 6
# Implementá una clase que represente una calculadora sencilla, que permita sumar, restar y multiplicar. 
# Este objeto debe entender los siguientes mensajes:
    #cargar(numero)
    #sumar(numero)
    # restar(numero)
    # multiplicar(numero)
    # valorActual()
# Si se evalúa la siguiente secuencia:
'''
calculadora = Calculadora()
calculadora.cargar(0)
calculadora.sumar(4)
calculadora.multiplicar(5)
calculadora.restar(8)
calculadora.multiplicar(2)
calculadora.valorActual()
'''
#CAMBIO 
# el resultado debe ser 24.

class Calculadora:
    def __init__ (self):
        self.valor = 0

    def sumar(self, numero):
        self.valor += numero 
    
    def restar(self, numero):
        self.valor -= numero
    
    def multiplicar(self, numero):
        self.valor *= numero 
    
    def valor_actualizado(self):
        return self.valor
    

# Ejercicio 7
# Definí una clase de gorriones, de los cuales nos interesa conocer dos medidas conocidas como CSS 
# (coeficiente de serenidad silenciosa), CSSP y CSSV (como el CSS pero “pico” y “veces”). 
# El CSS resulta de dividir la cantidad total de kilómetros que vuela desde que se lo comienza a estudiar, 
# por la cantidad total de gramos de comida que ingiere. El CSSP es la misma división pero considerando 
# solamente lo que voló la vez que más voló y lo que comió la vez que más comió. El CSSV es otra vez la misma idea,
# respecto de la cantidad de veces que voló y comió. Si un gorrión nunca comió, los coeficientes deben ser None.
# Un gorrión se considera en equilibrio si su CSS está entre 0.5 y 2.


class Gorriones:
    def __init__ (self):
        self.kilometros_totales = 0
        self.gramos_totales = 0
        self.kilometros_max = None
        self.gramos_max = None
        self.cantidad_vuelos = 0
        self.cantidad_comidas = 0

    def volar(self, kilometros):
        self.kilometros_totales += kilometros
        if self.kilometros_max is None or kilometros > self.kilometros_max:
            self.kilometros_max = kilometros
    
    def comer(self, gramos):
        self.gramos_totales += gramos
        if self.gramos_max is None or gramos > self.gramos_max:
            self.gramos_max = gramos
    
    def css(self):
        if self.gramos_totales == 0:
            return None
        return self.kilometros_totales/ self.gramos_totales
    
    def cssp(self):
        if self.gramos_max is None or self.kilometros_max is None:
            return None
        return self.kilometros_max/ self.gramos_max
    
    def cssv(self):
        if self.cantidad_comidas == 0:
            return None
        return self.cantidad_vuelos/self.cantidad_comidas
    
    def esta_en_equilibrio(self):
        css = self.css()
        return css is not None and 0.5 <= css <= 2