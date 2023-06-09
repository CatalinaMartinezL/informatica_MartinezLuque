import re

# Ejercicio 1
# Escribí un programa que verifique si un string tiene al menos 
# un carácter permitido. Estos caracteres son a-z, A-Z y 0-9.

def caracteres_permitidos(string):
    return bool(re.search('[a-zA-Z0-9]',string)) #bool() Devuelve un booleano  
    # Método .search() se utiliza para buscar un patrón de expresión regular en una cadena. Sintaxis: (PATRON, CADENA)
print(caracteres_permitidos("holacomoestas"))

# Ejercicio 2
# Escribí un programa que verifique si un string tiene todos 
# sus caracteres permitidos. Estos caracteres son a-z, A-Z y 0-9.

def todos_caracteres_permitidos(string):
    return bool(re.search('^[a-zA-Z0-9]*$',string))
#Explicación del patron
# ^: El símbolo "^" la búsqueda debe comenzar al inicio de la cadena.
# *: El símbolo "*" indica que el conjunto de caracteres anterior puede estar presente cero o más veces.
# $: El símbolo "$" indica que la búsqueda debe terminar al final de la cadena.

print(todos_caracteres_permitidos('HolaComo/esta4as'))

# Otra alternativa
def todos_caracteres_permitidos2(string):
    return not bool(re.search('[a-zA-Z0-9]', string))
# Al aplicar la función not a la salida de bool(re.search('[a-zA-Z0-9]', string)), el resultado 
# se invierte, lo que significa que la función devuelve True si la cadena está formada
#  completamente por caracteres permitidos, y False si hay al menos un carácter que no sea permitido.

# Ejercicio 3
# Creá un programa que verifique las siguientes condiciones:
# si un string dado tiene una h seguida de ninguna o más e.

def tiene_h(string):
    return bool(re.search("he*",string)) # *:0 o mas veces "e"

print(tiene_h("heeeeeeeeeeeee"))   
# Otra alternativa

def tiene_h2(string):
    return bool(re.search("he+",string)) # +: significa al menos 1 "e"

# si un string dado tiene una h seguida de cero o una e.
def tiene_h3(string):
    return bool(re.search('he?',string)) # ? <-- indica que la 'e' puede estar presente o no. Es decir, 0 o 1 vez

# si un string dado tiene una h seguida de dos o tres e.
def tiene_h4(string):
    return bool(re.search('he{2,3}',string)) # {2,3} : rango de veces que debe aparecer la 'e' 

print(tiene_h4('heee'))   

# Ejercicio 4
# Realizá un programa que encuentre una palabra unida a otra con un 
# guión bajo en un string dado (el string no debe contener espacios).

def dividido_por_guion(string):
    return bool(re.search('[a-zA-Z]+_+[a-zA-Z]+$', string)) 
# [a-zA-Z]+ <-- busca una o mas letras (primer palabra)
# _+ <-- busca uno o mas guiones 
# [a-zA-Z]+ <-- busca una o mas letras (segunda palabra)
# $ <-- Este símbolo indica el final de la línea.

print(dividido_por_guion('holalala_comoestas'))

# Ejercicio 5
# Escribí un programa que diga si un string empieza con un número específico.

def empieza_con_numero(string,numero):
    return bool(re.search('^'+str(numero), string)) 

print(empieza_con_numero('ho3la',3))

# Ejercicio 6
# Escribí un programa que dada una lista de strings verifique si se encuentran en una frase dada.

# Ejercicio 7
# Realizá un programa que encuentre un string que contenga
# solamente letras minúsculas, mayúsculas, espacios y números.
def min_num_espacios(string):
    return bool(re.search('[a-zA-Z0-9\s]+$',string))
    # [a-zA-Z0-9\s]+ representa uno o más caracteres que pueden ser una letra
    #  (mayúscula o minúscula) o un número o un espacio en blanco.

print(min_num_espacios('HOLA como estas tengo 20 años'))

# Ejercicio 8
# Escribí un programa que separe y devuelva los caracteres númericos de un string.

def numeros_en_string(string):
    return re.findall('[\d]',string) # .findall() devuelve todas las ocurrencias de un patrón en un string
# '\d' <-- refiere a caracteres numéricos.

print(numeros_en_string('holas 123 como 453 estas'))

# Ejercicio 9
# Escribí un programa que extraiga los caracteres que estén entre
# guiones en un string. (String de ejemplo: "Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-")

def separado_por_guiones(string):
    return re.findall(r'-(.*?)-',string)

# r: refiere a que la cadena es un raw string (los caracteres se toman como
# tal y no como metacaracteres Ej: \n --> \ n y no como salto de linea)
# - : el patrón comienza y termina con un guion
# (.*?) : es un grupo de captura que coincide con cualquier número de caracteres

print(separado_por_guiones('Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-'))

# Ejercicio 10
# Obtené las substrings y las posiciones de estas en un string
# dada considerando que las substrings están delimitadas por los caracteres @ o &.

def subustrings(string):
    return re.findall('[@|&](.*?)[@|&]',string) # no lo entiendo

print(subustrings('wdadawda @ dsede &awdawda&d@'))

# Ejercicio 11
# Realizá un programa que dado una lista de strings verifique que dos
# palabras dentro del string empiecen con la letra P y las imprima. 
# (Lista de ejemplo: ["Práctica Python", "Práctica C++", "Práctica Fortran"]).
def dos_p(lista):
    lista_p = []
    posicion = -1
    for string in lista:
        posicion +=1
        if re.search("(P\w*)\W(P\w*)",string):
            lista_p.append(lista[posicion])
    return lista_p

# (P\w*) : Primer bloque. Refiere a primer palabra.
#\w : caracters alfanumericos o _ [a-zA-Z0-9_]
# \W : separador palabras. Negación \w [^a-zA-Z0-9_]  ^ dentro del rango actua como negación, no para referirse al incio.
# (P\w*) : Segundo bloque. Refiere a segunda palabra.

print(dos_p(["Práctica Python", "Práctica C++", "Práctica Fortran", "Pala Pal"])) 


# Otra alternativa

def dos_P(lista):
    for elemento in lista:
        resultado = re.search("(P\w*)\W(P\w*)", elemento) # en clase vimos metodo .match(), q solo busca al inico de la cadena.
        if resultado is not None:
            print(resultado.group())

print(dos_P(["Práctica Python", "Práctica C++", "Práctica Fortran", "Pala Pal"]))


# Ejercicio 12
# Escribí un programa que reemplace todas las ocurrencias 
# de espacios, guiones bajos y dos puntos por la barra vertical (|).

def reemplazar_caracteres(string):
    return re.sub('[\s_:]','|',string)

print(reemplazar_caracteres('hola_como;estas :'))

# Ejercicio 13
# Escribí un programa que reemplace los dos primeros caracteres
# no alfanúmericos por guiones bajos.

def no_alfanumericos(string):
    return re.sub('[^a-zA-Z0-9]','_',string, count=2)

print(no_alfanumericos('hola .como/estas'))

# Ejercicio 14
# Realizá un programa que reemplace los espacios y
# tabulaciones por punto y coma.

def reemplazar_espacio_tab(string):
    return re.sub('[\s\t]+',';',string)

print(reemplazar_espacio_tab('hola como estas   '))

# Ejercicio 15
# Realizá un programa que validar si una cuenta de mail está escrita correctamente.

def mail_correcto(string):
    return bool(re.search('^\w+[.-]?\w*@[a-zA-Z]+[.][a-z]+[.]?[a-z]?$',string))
# visto en clase

# EXPLICACIÓN PATRÓN:
# ^\w+[.-]?\w* : inicia con 1 o mas caracteres alfanumericos, que pueden estar seguidos o no de u '.' o '-', a lo que le pueden seguir o no otros caracteres alfanumércios .
# @ : le debe seguir una @ obligatoriamente
# [a-zA-Z]+[.][a-z]+ : a continuacion el dominio (incluye solo letras minusculas ej: 'gmail'). Luego separa un '.' obligatoriamente del 'com' o 'edu'
# [.]?[a-z]? : puede incluir el '.ar' por ejemplo. NO es necesacrio que lo incluya
# $ : Fin de string. Incluir si o si si incluyo el ^ al inicio para 