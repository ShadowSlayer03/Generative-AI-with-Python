from datetime import datetime
from typing import List

from pydantic import BaseModel, ConfigDict


class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    created_at: datetime
    address: Address
    tags: List[str] = []

    model_config = ConfigDict(
        json_encoders={datetime: lambda v: v.strftime('%d-%m-%Y %H:%M:%S')}
    )

user = User(
    id=1,
    name="Arjun",
    email="hoho@gmail.com",
    created_at=datetime(2024, 3, 15, 14, 30),
    address=Address(
        street="XYZ St",
        city="ABC City",
        zip_code="123233"
    ),
    is_active=False,
    tags=["premium", "subscriber"]
)

python_dict = user.model_dump()

print(user)
print("="*40)
print(python_dict)
print("="*40)
json_str = user.model_dump_json()
print(json_str)
