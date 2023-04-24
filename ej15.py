#!/usr/bin/env python3

import re

def mail_correcto(string):
    return bool(re.search('^\w+[.-]\w*[@][a-z]+[.]?[a-z]+[.]?[a-z]?$'), string)
print(mail_correcto('catalinamartinezluque@gmail.com'))
print(mail_correcto('catalina&martinezluqu@gmail.com'))

# polimorfismo: la clase que envía el mensajes y al menos dos clases mas que lo utilicen 
# un mismo mensaje, pero con distintos resultados entre clases
# los atributos siempre se definen en el init de la clase, y llevan el self. adelante, tomando un parámetro dado
# Estado = conjunto de atributos
# Interfaz = conjunto de mensajes/métodos que aborda una clase
