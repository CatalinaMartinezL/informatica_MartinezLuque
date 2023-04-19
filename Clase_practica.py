# Práctica de Expresiones regulares
# Ejercicio 1
import re

def caracteres_permitidos(string):
    return bool(re.search('[a-zA-Z0-9.]', string))

# Ejercicio 2
def caracteres_permitidos(string):
    return not bool(re.search('[a-zA-Z0-9.]'))

# Ejercicio 3
def encontrar_patron(string):
    patron = "he*"
    if re.search(patron, string) is not None:
        return "se encontro el patron"
    else:
        return "No se encontro el patron"
    
def encontrar_patron(string):
    patron = "he?"
    if re.search(patron, string) is not None:
        return "se encontro el patron"
    else:
        return "No se encontro el patron"
    
def encontrar_patron(string):
    patron = "he{2,3}"
    if re.search(patron, string) is not None:
        return "se encontro el patron"
    else:
        return "No se encontro el patron"
    
# Ejercicio 4
def palabras_unidas(string):
    patron = "^[a-z]+_[a-z]+$"
    if re.search(patron, string) is not None:
        return "Patron encontrado"
    else:
        return "Patron encontrado"

# Ejercicio 8
def extraer_numeros(string):
    resultado= re.split("\D+", string)
    for elemento in resultado:
        print(elemento)

# Ejercicio 9
def entre_guiones(string):
    return re.findall(r"-(.*?)-", string)

string = "Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-"

# Para el operador logico or = | 
# Para el operador logico and = &

# Ejercicio 11
def dos_P(lista):
    for elemento in lista:
        resultado = re.match("(P\w*)\W(P\w*)", elemento)
        if resultado is not None:
            print(resultado.group())

lista = ["Práctica Python", "Práctica C++", "Práctica Frontran"]
print(lista)

#Tarea ejercicio 15