from jinja2 import Environment
from jinja2 import FileSystemLoader
from wsgiref.simple_server import make_server

#Funcion encargada de responder a cada una de las peticiones del cliente
# 2 parametros
# env -> diccionario con informacion relevante con respecto a la peticion. Se conoce el metodo
# start_response -> callback, recibe 2 argumentos(status code, listado de encabezado que se envien al cliente)
#encabezados seran lista de tuplas
def application(env, start_response):
    #Indicar que tipo de respuesta va a recibir
    headers = [('Content-Type', 'text/html')]
    start_response('200 OK', headers)

    env = Environment(loader = FileSystemLoader('templates'))
    template = env.get_template('index.html')

    html = template.render(
        {
            'title':'Servidor en Python',
            'name':'Jorge Ariza Ramirez'
        }
    )

    return [bytes(html, 'utf-8')]

#direccion en el que se ejecuta el servidor
#puerto
#funcion a responder a cada una de las peticiones
server = make_server('localhost', 8000, application)
#Que se encuentre a la escucha
server.serve_forever()