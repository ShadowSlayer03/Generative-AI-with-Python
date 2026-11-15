from pydantic import BaseModel, field_validator, model_validator


class User(BaseModel):
    username: str

    # Field validators can be used to ensure that a specific field follows a particular criteria or pattern etc
    @field_validator('username')
    def username_length(cls, v):
        if len(v) < 4:
            raise ValueError("Username must be atleast 4 characters long!")
        return v

class SignupData(BaseModel):
    password: str
    confirm_password: str

    # Model validators are used for comparing or working with multiple fields within the model
    @model_validator(mode='after')
    def check_both_are_same(self):
        if self.password.strip() != self.confirm_password.strip():
            raise ValueError("Passwords do not match, please try again!")
        return self
