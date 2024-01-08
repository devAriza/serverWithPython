from pydantic import BaseModel, ValidationError, field_validator, validator
from typing import Optional

class User(BaseModel):
    username: str #requerido
    password: str
    repeat_password: str
    email: str
    age: Optional[int] = None

    #referencia a clase y atributo
    #decorador con parametro el atributo
    @field_validator('username')
    def username_validation_lenght(cls, username):
        if len(username) < 3:
            raise ValueError('La longitud minima es de 4 caracteres.')

        if len(username) > 50:
            raise ValueError('La longitud maxima es de 50 caracteres.')

        return username

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
        email = 'info@codigofacilito.com',
        age = 10
        )

    print(user1)
    
except ValidationError as e:
    print(e.json())
