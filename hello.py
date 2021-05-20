from flask import Flask

app = Flask(__name__) #crear instancia de Flask(aplicación)
@app.route('/') #decorador metodo route asocia contenido a la segunda ruta '/'
def index():
  return 'Hola, nundo!' 

@app.route('/adios')
def bye():
  return 'Hasta luego, cocodrilo'  