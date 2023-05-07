# definir un procedimiento que lea los archivos .txt que estan en la carpeta
# marzo, y copie la primera linea de cada uno en un archivo dentro de la carpeta
# resultados (que debe estar dentro de new)

#!/usr/bin/env python3
# lo uso para que cuando ejecute mis ejercicios no tenga que escribir python y el nombre del 
# script, solo pyhton

import os, glob, sys

def primeras_lineas(path_a_txt, path_resultado, salida):
    #movemos a marzo
    #extraemos los .txt
    #leemos las primeras lineas
    #hacemos carpeta de salida
    #crear archivo
    #poner lineas en archivo nuevo
    os.chdir(path_a_txt)
    textos = glob.glob("*.txt")
    primer_linea = []
    for txt in textos:
        with open(txt, "r") as texto:
            primer_linea.append(texto.readline())
    
    os.chdir("../../")
    os.mkdir(path_resultado)
    os.chdir(path_resultado)
    with open(salida, "a") as final_txt:
        for linea in primer_linea:
            final_txt.write(linea)

primeras_lineas("datos/marzo", "resultado", "salida.txt")