from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    is_active: bool

input_data = {
    'id': 101,
    'name': 'Kumar',
    'is_active': True
}

# Pydantic tries to convert things into proper types if possible
# Eg strings into desired types like integer or bool, hence even if we provide 'True' or '101' it not raise a ValidationError
user = User(**input_data)
print(user)
