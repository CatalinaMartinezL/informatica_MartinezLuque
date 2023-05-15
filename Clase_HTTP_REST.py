# instalar requests
# CLIENTE Y SERVIDOR: Computadoras con distinto rol, el segundo
# aporta algo (contenido, datos). El cliente consume aquel aporte
# El tamaño de hardware es relativo
# En principio se usan las mismas tecnologías, cambian las necesidades

# PROTOCOLO DE COMUNICACIÓN: mas usado HTTP, para la comunicación entre 
# el cliente y el servidor

# WEB APP
# ---> persiste(guarda) info ---> data based
# tiene una ase de datos asociada y la lógica para manejar y almacenar esos datos
# muchos archivos html interconectados - sitio web

# PÁGINA WEB
# un archivo Html expuesto en la nube

# APLICACIÓN REST: recursos
# la url determina a un recurso (lo que viene despues de la barra)
# ej: https:/listado.mercadolibre.com/LIBROS...
# 'http': protocolo con el que me comunico al servidor, en este caso al de mercado libre
# 'https', el mismo protocolo que el anterior, nada mas que se le agrega s de security

import requests 

# biblioteca de python que nos permite manejar pedidos, http
respuesta = requests.get("https://api.github.com/users/ajvelezrueda/orgs") 
datos = respuesta.json() # tare una lista, con diccionarios
print(datos)
# trae la columna code
# le pregunto al servidor, el cual tiene la logica para procesar la base de datos. Estoy del lado del cliente
# get ---> verbo http asociado a las consultas. El que busca es el servidor, el get el cliente -PROTOCOLO- 
#          dispara acciones que consulten a la base de datos
# los verbos http disparan acciones particulares, siempre hablando de aplicaciones rest (bien programadas)

# HTTP tiene 4 verbos que vamos a usar:
#       1- get
#       2- post: esta asociado a escribir o persistir datos (de cero)
#       3- delete: se encarga de borrar datos de algun recurso
#       4- patch: verbo asociado a reescribir datos
#       5- json: estructura de diccionario, tiene sus claves y sus valores

respuesta = requests.get("https://api.github.com/users/ajvelezrueda/orgs") 
datos = respuesta.json()
# 1)  en cunatas orgas está involucrado el usuario
print(len(datos))
# 2) lista de nombres delas orgas en la que está involucrado

print(respuesta)
print(respuesta.headers) # headers me da informacion sobre el propio pedido, cuando se hizo, a que servidor
#                          me da el limite tambien, el formato en el que esta

print(respuesta.status_code)