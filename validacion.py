from pydantic import BaseModel, validator, ValidationError
from typing import Optional

class User(BaseModel):
    username: str #requerido
    password: str
    email: str
    age: Optional[int] = None

    #referencia a clase y atributo
    #decorador con parametro el atributo
    @validator('username')
    def username_validation_lenght(cls, username):
        if len(username) < 3:
            raise ValueError('La longitud minima es de 4 caracteres.')

        if len(username) > 50:
            raise ValueError('La longitud maxima es de 50 caracteres.')

        return username
        
try:
    user1 = User(
        username = 'KK',
        password = 'password123',
        email = 'info@codigofacilito.com',
        age = 10
        )

    print(user1)
    
except ValidationError as e:
    print(e.json())
