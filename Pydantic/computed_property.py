from pydantic import BaseModel, Field, computed_field


class Product(BaseModel):
    price: float
    quantity: int

    @computed_field
    @property
    def total_price(self) -> float:
        return self.price * self.quantity


class Booking(BaseModel):
    user_id: int
    room_id: int
    nights: int = Field(
        ...,
        ge=1
    )
    rate_per_night: float

    @computed_field
    @property
    def total_amount(self)->float:
        return self.nights * self.rate_per_night

booking = Booking(
    user_id=123,
    room_id=202,
    nights=3,
    rate_per_night=100.25
)

print("Total amount:", booking.total_amount)
print("Model dump:", booking.model_dump())
