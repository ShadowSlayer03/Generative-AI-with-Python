from typing import Dict, List, Optional

from pydantic import BaseModel, Field


class Employee(BaseModel):
    id: int
    name: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description="Employee name",
        examples="Kumar Sanu"
    )
    department: Optional[str] = 'General'
    salary: float = Field(
        ...,
        ge=10000,
        le=10000000
    )


class User(BaseModel):
    email: str = Field(
        ...,
        regex=r''
    )
    phone: str = Field(
        ...,
        regex=r''
    )
    age: int = Field(
        ...,
        ge=0,
        le-150
        description="Age of the customer"
    )
