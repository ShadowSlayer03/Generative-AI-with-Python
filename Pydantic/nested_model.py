from typing import List, Optional

from pydantic import BaseModel


class Address(BaseModel):
    street: str
    city: str
    postal_code: str

# User contains a reference of the Address model here
class User(BaseModel):
    id: int
    name: str
    address: Address

address = Address(
    street="XYZ Street",
    city="ABC City",
    postal_code="AJHFBSD134"
)

user = User(
    id=1,
    name="Arjun",
    address=address
)

user_data = {
    "id": 1,
    "name": "Hitesh",
    "address": {
        "street": "123 something",
        "city": "Paris",
        "postal_code": "2322323"
    }
}

user = User(**user_data)

print(user.model_dump())
