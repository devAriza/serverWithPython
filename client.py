from urllib import request

URL = 'http://localhost:8000/'

response = request.urlopen(URL)
#conocer atributos del objeto
print(response.__dict__)
#obtener el contenido de la respuesta del servidor
print(response.read())


