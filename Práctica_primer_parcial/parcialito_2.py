# Ejercicio 1
# Escribir funciones que, dado un String, permitan responder lo siguiente:
# a) obtener la lista de los substrings delimitados entre '<' y '>' 
# que no incluyan ninguna 'o'.

import re

def delimitados_piquitos_sin_o(string):
    print(re.findall("<([^o]*?)>", string))

# El corchete [] se utiliza para definir una clase de caracteres, y 
# el símbolo ^ dentro de la clase se utiliza como negación, 
# lo que significa que coincide con cualquier carácter que no esté dentro
# de la clase especificada.

print(delimitados_piquitos_sin_o("hola<como estas?> soy <catalina> y tengo 20 años"))

# b) Onomatopopih, que aún no sabe mucho de expresiones regulares,
# nos mandó una función que debería ser capaz de decirnos si un string incluye o no un substring de 3 letras,
# cada una de las cuales debe ser a, b ó c. Esto es, alcanza con incluir, p.ej, 'abc', 'cbc', 'aac', 'ccc'.

# En base a la función que definió respondé:

# ¿Qué error/es tiene? (justificando la respuesta).
# Uno de los errores esta en el patron, el metacaracter {3} solo influye en la c; y tampoco da lugar a que haya match con las 3 letras en otro orden
# Tendria que usar re.search para que la funcion nos diga SI INCLUYE O NO el substring. Con el findall, si la funcion esta escrita correctamente,
# devolvera la lista de coincidencias. 

# Modificá la función para que cumpla lo requerido correctamente.

def triples(string):
    return re.findall("abc{3}", string)

print(triples("svsslkvabckjsv"))


def triples_correcta(string):
    print(bool(re.search("[a-c]{3}", string)))

# probando 
print(triples_correcta("svsslkvkjabcuhjv"))
print(triples_correcta("svsslkvkjbbcuhjv"))
print(triples_correcta("svsslkvkjabuhjv"))
print(triples_correcta("svssalkvbkjcuhjv"))

# Ejercicio 2
#  Dada la siguiente clase resolvé los siguientes ejercicios y respondé las preguntas:

class BrujoHogwarts:
    def __init__(self, mascota, casa, escoba):
        self.puntos = 10
        self.mascota = mascota
        self.casa = casa
        self.escoba = escoba

    def get_mascota(self):
        return self.mascota

    def get_casa(self):
        return self.casa

    def entrenar_quidditch(self, escoba_alternativa):
        self.escoba == escoba_alternativa
        self.puntos += 1

    def jugar_quidditch(self):
        self.puntos += 4
    
    def recitar_himno_de_casa(self):
        print("Y cuando al final de los siete años te marches por rumbos inciertos y extraños llévate el espíritu de Hogwarts contigo.\n¡Y que Gryffindor guíe tu camino!")

# a) ¿Cuál es el nombre de la clase? El nombre de la clase es BrujoHogwarts
 
# ¿Cuál es el estado de un BrujoHogwarts? El estado de BrujoHogwarts es self.puntos, self.mascota, self.casa, self.escoba
 
# ¿Qué mensajes entiende el BrujoHogwarts? El BrujoHogwarts entiende get_mascota, get_casa y entrenar_quidditch

# b) Instanciá al BrujoHogwarts Harry, que es tiene como mascota una lechuza, es de la casa de gryffindor,
# tiene una escoba nimbus 2000

harry = BrujoHogwarts("lechuza", "gryffindor", "nimbus 2000")

# c) Definir el método jugar_quidditch que por anota 4 puntos de Harry
# d) Definir un método recitar_himno_de_casa que retorne las últimas dos frases del himno de la casa, las cuales son:

# "Y cuando al final de los siete años te marches por rumbos inciertos y extraños llévate el espíritu de Hogwarts contigo.
# ¡Y que Gryffindor guíe tu camino!"

print(harry.puntos)
print(harry.casa)
print(harry.escoba)
print(harry.mascota)
print(harry.recitar_himno_de_casa())
harry.jugar_quidditch()

# Ejercicio 3
# A) En los textos mágicos .log se encuentra escondido el discurso del sombrero seleccionador.

# Usando todo lo que sabes de las bibliotecas os, glob y re construí un procedimiento que:
# i) cree un directorio cuyo nombre se corresponde con el nombre de la casa elegida,
# la cual se esconde en la 4ta linea del archivo texto5.log.

# ii) extraiga las primeras 4 líneas de los archivos .log

# y las almacene en un único archivo llamado selección_del_sombrero.txt,

# que se guarde en la carpeta creada en el punto i).

import os, glob, re 

def encontrar_discurso(archivo):
    os.mkdir("Gryffindor")                      #creo gryf

    discurso = glob.glob("*.log")               #todos los archivos log 

    for a in discurso:                       # por cada archivo log 

        with open (a, "r") as file:          #abrilo
            palabras = file.readlines()                  #lee las primeras 4 lineas 
            
            with open ("Gryffindor/"+ archivo, "a") as file2:            #abri selec
                file2.write(str(palabras[0:4]))

encontrar_discurso("selección_del_sombrero.txt")

# Ejercicio 4
# a) Onomatopopih está aprendiendo expresiones regulares y le pidieron construir una función que sea capaz de extraer un teléfono de
# 8 números que comienza con 4, a partir de un archivo base_de_telefonos.txt.

# Revisá su código propuesto y marcá con una [x] las opciones correctas.
# JUSTIFICA tus respuestas.


def extractorDeTel(path):
    with open(path, 'w') as miarch:
        texto = miarch.read()
        return re.match("4([0-9]{8})", texto)

# La función devuelve NameError al ser ejecutada.
# Va a dar NameError si no llamamos a la biblioteca RE!!

# La función devuelve SyntaxError al ser ejecutada

# [x] La función devuelve io.UnsupportedOperation al ser ejecutada. 
# Porque el archivo se abre en modo w (write) y en la siguiente linea el archivo se lee (con el modo .read())

# Cuando se invoca la función extractorDeTel usando el texto 'oahsdgfjhdgfjagdsfjsdgfkdgfks42948555' devuelve 4
# Cuando se invoca la función extractorDeTel usando el texto 'oahsdgfjhdgfjagdsfjsdgfkdgfks42948555' devuelve 42948555

# Las dos opciones de aca arriba, asi como esta dada la fucion, son incorrectas.
# El patrón no es el correcto para extraer un teléfono de 8 números que comienza con 4
# "^4[0-9]{7}" este patron podria funcionar, no llegue a porbarlo :(

# [x] Para compartir los cambios con sus compañeros Onomatopopih debe escribir git add . en la terminal y luego git commit -m "mi mensaje" y git push.
# CORRECTO Una vez que termino y guardó sus cambios, deberá realizar esos tres pasos, en ese orden, para actuzalizar el repositorio compartido. 
# Cabe aclarar que antes de realizar sus cambios y esa serie de pasos, debe hacer un git pull para descargar los aportes de sus compañeros, si es que se realizo alguno.

# Para compartir los cambios con sus compañeros Onomatopopih debe primero escribir git commit -m "mi mensaje" y git push

# Para descargarse los aportes de sus compañeros Onomatopopih debe escribir en la terminal git push
# [x] Para descargarse los aportes de sus compañeros Onomatopopih debe escribir en la terminal git pull.
# CORRECTO. Con el git pull descarga el aporte de sus compañeros 

# Ejercicio 5
# Los árboles de casi todas las especies se comportan de manera similar, casi sin importar las condiciones de luz o climáticas.

# Se propone modelar este comportamiento en una clase, sabiendo que los árboles tienen como principal característica
# si son perennes (no pierden las hojas), una cantidad de agua, nutrientes y altura.

class Arbol:
    
    def __init__(self, agua = 0, nutrientes = [], altura = 0):
        self.agua = agua
        self.nutrientes = nutrientes
        self.altura = altura
        self.son_perennes = True 

    def hacer_fotosistesis(self, tiempo):
        self.nutrientes = self.nutrientes +  (1 * (tiempo/10))
    
    def absorber_agua(self, cantidad):
        self.agua +=cantidad
    
    def crecer(self):
        if self.nutrientes == 100 and self.agua == 100:
            self.altura += 1

# hacer_fotosistesis(tiempo), la cual aumenta los nutrientes de la misma (1 punto cada 10 minutos),
# absorber_agua(cantidad), el cual aumenta el agua en cierta cantidad
# crecer(), en el cual, si se cumplen las condiciones de nutrientes y agua (100 puntos de cada uno),
# se aumenta la altura en 1 cm.

# El manzano tiene como característica un poco más particular,
# que genera frutos, las manzanas.

# Esto hace que la planta gaste energía en formar estos frutos,
# por lo que para crecer 1 cm necesita 150 puntos de agua
# y 200 de nutrientes.
# Además este árbol no es perenne.

class Manzano(Arbol):

    def __init__(self):
        self.son_perennes = False
    
    def crecer(self):
        if self.nutrientes == 200 and self.agua == 150:
            self.altura += 1

# Definí las clases Arbol y Manzano,
# hacé que esta último herede de la primera agregando y/o redefiniendo los métodos necesarios.
