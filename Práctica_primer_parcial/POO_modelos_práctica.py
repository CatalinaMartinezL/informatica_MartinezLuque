# En un mundo distópico la humanidad es atacada sin descanso por titanes. Estos titanes son muy resistentes pero no inmortales, 
# su salud (100 de máxima) puede ir disminuyendo si reciben daño debido a algún ataque, y si llega a 0 se muere. 
# Al recibir este ataque la salud disminuye 1.5 por cada puntos de daño recibido. 
# Además tienen la capacidad de destruir cierto número de casas dependiendo de su salud, siendo 8 casas cuando su salud 
# es máxima o un número proporcional si su salud es menor a la máxima (si tiene 60 puntos de salud destruiría 4.8 casas,
# es decir, 4 casas completas y más de la mitad de otra). Sin embargo no tienen la capacidad de comunicarse con los humanos, 
# siendo un grito, "¡Aaaarrrg!", el único sonido que hacen. Definí la clase Titan con los atributos y métodos correspondientes.
# Además instanciá a un Titan y ejecutá las siguientes líneas:

class Titan:
    def __init__(self, salud_actual):
        self.salud = salud_actual 
        salud_actual = 100
        self.max_salud = 100
    
    def salud_actual(self):
        return self.salud

    def esta_vivo(self):
        return self.salud > 0
    
    def recibir_ataque(self, cantidad_de_ataques):
        self.salud -= 1.5*cantidad_de_ataques

    def cantidad_casas(self):
        return self.salud*8/self.max_salud

    def destruir_casas(self):
        if (self.cantidad_casas() > 1):
            if((self.cantidad_casas() % 1) > 0):
                self.salud -= (self.cantidad_casas() // 1) * 12.5
            else:
                self.salud -= (self.cuantas_casas() -1) * 12.5
        else:
                print("No puede destruir ninguna casa")
    def gritos(self):
        return "¡Aaaarrrg!"
    
titan1 = Titan(100)
titan1.recibir_ataque(30)
print(titan1.esta_vivo())
print(titan1.salud_actual())
print(titan1.cantidad_casas())
print(titan1.gritos())
titan1.destruir_casas()
titan1.salud_actual()
titan1.recibir_ataque(4)
print(titan1.esta_vivo())


# Potencia de 0 a 100
# coraza de 0 a 20
# pila atómica aumenta la potencia en 25
# escudo aumenta la coraza en 10
# detiene el ataque con la coraza, si no alcanza sigue con la potencia
# si la Enterprise no tiene nada de coraza, se descuentan de la potencia
# no pueden quedar en negativo, a lo sumo en 0
# nace con 50 de potencia y 5 de coraza
# potencia()
# coraza()
# encontrarPilaAtomica()
# econtrarEscudo()
# recibirAtaque(puntos)