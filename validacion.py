<<<<<<< HEAD
from pydantic import BaseModel, ValidationError, field_validator, validator
=======
from pydantic import BaseModel, validator, ValidationError
>>>>>>> 5b6f48f2c91d07d5d2cabedd960023076621a9d9
from typing import Optional

class User(BaseModel):
    username: str #requerido
    password: str
<<<<<<< HEAD
    repeat_password: str
=======
>>>>>>> 5b6f48f2c91d07d5d2cabedd960023076621a9d9
    email: str
    age: Optional[int] = None

    #referencia a clase y atributo
    #decorador con parametro el atributo
<<<<<<< HEAD
    @field_validator('username')
=======
    @validator('username')
>>>>>>> 5b6f48f2c91d07d5d2cabedd960023076621a9d9
    def username_validation_lenght(cls, username):
        if len(username) < 3:
            raise ValueError('La longitud minima es de 4 caracteres.')

        if len(username) > 50:
            raise ValueError('La longitud maxima es de 50 caracteres.')

        return username
<<<<<<< HEAD

    @validator('repeat_password')
    def repeat_password_validation(cls, repeat_password, values):
        if 'password' in values and repeat_password != values['password']:
            raise ValueError('Las contrasenias son diferentes')

        return repeat_password
        
try:
    
    user1 = User(
        username = 'Jorge',
        password = '123',
        repeat_password = '123',
=======
        
try:
    user1 = User(
        username = 'KK',
        password = 'password123',
>>>>>>> 5b6f48f2c91d07d5d2cabedd960023076621a9d9
        email = 'info@codigofacilito.com',
        age = 10
        )

    print(user1)
    
except ValidationError as e:
    print(e.json())
