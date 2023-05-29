from flask import Flask
prendas = [
    {"id": 2, "tipo": "pantalon", "talle": 42},
    {"id": 2, "tipo": "pantalon", "talle": 56},
]
app = Flask(__name__) 

@app.get("/")
def home ():
    return "<p>Te damos la bienvenida a MacoWins</p>" 

# Tarea: armar la ruta /prendas que muestre todos los items de prendas