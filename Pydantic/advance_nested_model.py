from typing import List, Optional, Union

from pydantic import BaseModel


#########
# Optional Nested Model
#########
class Address(BaseModel):
    street: str
    city: str
    postal_code: str

class Company(BaseModel):
    name: str
    address: Optional[Address] = None

class Employee(BaseModel):
    name: str
    company: Optional[Company] = None

#########
# Mixed Data type
#########
class TextContent(BaseModel):
    type: str = "text"
    content: str

class ImageContent(BaseModel):
    type: str = "Image"
    url: str
    alt_text: str

class Article(BaseModel):
    title: str
    sections: List[Union[TextContent, ImageContent]]

#########
# Deeply Nested Structure
#########
class Country(BaseModel):
    name: str
    code: str

class State(BaseModel):
    name: str
    country: Country

class City(BaseModel):
    name: str
    state: State

class Address(BaseModel):
    street: str
    postal_code: str
    city: City

class Organization(BaseModel):
    name: str
    head_quarter: Address
    branches: List[Address]=[]
