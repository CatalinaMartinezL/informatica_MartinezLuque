import requests

respuesta = requests.get("https://pokeapi.co/api/v2/pokemon/ditto")
# Para que una api sea rest tiene que la url mapear recursos.
# Html, trabaja con textos

# 1)Describir las partes de la url:
# "https": protocolo que utilizo para comunicarme al servidor
#         (de una computadora a otra), de manera segura.
#          Solo soporta texto.
# "/api/v2/pokemon/ditto": recurso, las cosas que puedo consultar de la
#                         base de datos.
#                         El recurso cambia dependiendo lo pedido
# "pokeapi.co": dominio, con el cual voy a mapear una ip
# Una url es similar a un path 


# 2)¿Qué respuesta obtenes al hacer un get a esa url?
# Me devuelve todos los contenidos asociados al recurso ditto, con los 
#       de sus habilidades, experiencias, formas, etcétera.
respuesta = requests.get("https://pokeapi.co/api/v2/pokemon/ditto")
contenido_respuesta = respuesta.json()
print(contenido_respuesta.keys())

# 3) ¿Cuál es el content type de esa respuesta
print(respuesta.headers["Content-Type"])
# Devuelve la aplicación que utiliza, en este caso json

# 4) ¿Cuál es el status code de la respuesta?
print(respuesta.status_code)
# 200 significa que estaba todo bien

# 5) ¿Cuántas habilidades tiene este pokemon?
print(f'tiene {len(contenido_respuesta["abilities"])} habilidades') 
print(contenido_respuesta["abilities"])


# Estructura de un proyecto Flask
# Flask
#   -----> app.py: tenemos los endpoints(rutas) de mi API
#   -----> templates: vamos a tener todas las pantallas de mi aplicación (archivos HTML)
#   -----> static: 
#              ----> CSS: aca voy a tener los estilos de mi pantalla
#   -----> assets: acá irían todos los recursos extras(imágenes, logos, etc)