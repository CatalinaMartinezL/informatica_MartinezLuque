# Ejercicio 1
# Escribir funciones que permitan obtener el anterior y 
# el siguiente de un número.

def anterior(numero):
    return numero-1

def siguiente(numero):
    return numero+1

print(anterior(8))
print(siguiente(10))

# Ejercicio 2
# Escribir una función que obtenga el doble de un número.

def doble(numero):
    return numero*2

print(doble(5))


# Ejercicio 3
# Escribir funciones que obtengan el doble del anterior y el doble del siguiente de un número.

def doble_anterior_siguiente(num):
    return str(doble(anterior(num))) +' '+ str(doble(siguiente(num))) 

print(doble_anterior_siguiente(10))


# Ejercicio 4
# Escribir una función llamada retirar_dinero, que tenga como parámetros el saldo y el monto 
# a retirar y que devuelva cuánto saldo queda luego de la extracción.P Si retira más dinero 
# que lo que tiene en el saldo debe devolver 0 (no se puede usar if)

def retirar_dinero(saldo, monto_retirar):  
 return  max(saldo-monto_retirar,0) 

print(retirar_dinero(34000,12000))
print(retirar_dinero(20000,54000))

# Ejercicio 5
# Escribir una función llamada dia_de_la_semana_favorito que tome como parámetro un día de la 
# semana y devuelve True si el día es "Sábado" o False si es cualquier otro (no se puede usar if).

def dia_de_la_semana_favorito(dia):
    return dia == "Sábado"

print(dia_de_la_semana_favorito("Sábado"))
print(dia_de_la_semana_favorito("Lunes"))
print(dia_de_la_semana_favorito("Jueves"))


# Ejercicio 6
# Escribir una función que determine si una longitud de onda de una radio está dentro o fuera del 
# rango de recepción de una antena. La longitud de onda mínima que recibe la antena es 223.0
#  y la máxima es 586.8 (no se puede usar if).

def longitud_onda(onda):
    return 223<=onda<=586.8

print(longitud_onda(335.7))
print(longitud_onda(789.8))


# Ejercicio 7
# Reescribir la función del punto anterior considerando, además, que la longitud de onda 
# no puede ser 314.5 porque ya está ocupada por otra radio (no se puede usar if).    

def longitud_onda(onda):
    return 223<=onda<=586.8 and onda != 314.5

print(longitud_onda(314.5))
print(longitud_onda(322.2))

# Ejercicio 8
# Escribir una función llamada tiene_descuento que tome como parámetro una edad y devuelva 
# True en caso de que la edad sea menor o igual a 12 o mayor o igual a 60. En caso contrario 
# tiene que devolver False (no se puede usar if).

def tiene_descuento(edad):
    return 12>=edad or edad>=60

print(tiene_descuento(12))
print(tiene_descuento(78))
print(tiene_descuento(17))


# Ejercicio 9
def xor (booleano1, booleano2):
    return booleano1 != booleano2

print(xor(True, True))
print(xor(True, False))


# Ejercicio 10
def saludo (nombre, apellido):
    return "Hola " + nombre + ", en que andan los " + apellido + "?"

print(saludo("Catalina", "Galnares"))


# Ejercicio 11

def empieza_con_h (palabra):
    if palabra.startswith('h'):
        return len(palabra)
    else:
        return "La palabra no empieza con h"

print(empieza_con_h('armario'))
print(empieza_con_h('hipertrofia'))

# Ejercicio 12
def buenos(f):
    return f.startswith("Buenos") or f.startswith("Buenas")

print(buenos("Buenos dias"))
print(buenos("Hola, buen dia"))

# Ejercicio 13
def es_multiplo (num1, num2):
    return num2 % num1 == 0

print(es_multiplo(5, 10))
print(es_multiplo(2, 11))

# Ejercicio 14
def par_impar_cero (num):
    if num % 2 == 0 and num != 0:
        return "es par"
    elif num % 2 != 0:
        return "es impar"
    else:
        return "es cero"

print(par_impar_cero(4))
print(par_impar_cero(3))
print(par_impar_cero(0))

# Ejercicio 15
def a_en_frase (frase):
    ases = 0
    for letra in frase:
        if letra == "a" or letra == "A":
            ases += 1
    return ases

print(a_en_frase("hola, cómo estas"))
print(a_en_frase("hola, cómo estAs"))
print(a_en_frase("el estruendo se sintió"))


# Ejercicio 16
def cuantos_meses_me_quedan_de_vida (dinero):
    return dinero / 60000

print(cuantos_meses_me_quedan_de_vida(3450000))
