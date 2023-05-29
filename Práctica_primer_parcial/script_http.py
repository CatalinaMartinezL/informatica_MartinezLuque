import requests

rta = requests.get('https://pokeapi.co/api/v2/ability/150/')
print(rta.json())
# contiene una descripcion, en este caso una habilidad
# "/150/'": parámetro
# con un /recurso con un get traigo todos los items del recurso
# /recurso/ id: me trae el id particular de ese recurso

# ej: 
rta = requests.get('https://macowins-server.herokuapp.com/prendas?tipo=pantalon')

# https: //_______/ recurso --->get---> listar todos los items de ese recurso
# ______/ recurso/id ---> get ---> muestra un ítem del recurso en particular
#                    ---> delete---> borra ese item
#                    ---> patch---> modifica una parte del item 
#                    ---> post ---> reescribir de cero
#                    ---> put ---> modficia todo el item
# ______/ recurso?___ = ____ --->get---> todos los itmens que tienen ese valor en esa key
#               query params
# si uso & con los query params, puedo concatenar otros filtrados

# BIBLIOTECA FLASK
# me permite ver todo lo que estoy haciendo, un post, un patch
# tiene frame works, genera el back(datos, requests)
# en algun momento puede generar el front(interaccion con el usuario)

# API ----> rutas(endpoints) ---> url en las cuales se accede a los recursos