from pydantic import BaseModel


class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = False

product1 = Product(id=1, name="Laptop", price=450.00, in_stock=True)

product2 = Product(id=2, name="Keyboard", price=24.25, in_stock=True)

# Wrong usage will throw ValidationError
# product3 = Product(id=3, name="Keyboard")
