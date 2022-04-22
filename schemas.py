import pydantic as _pydantic
import datetime as _datetime

class UserBase(_pydantic.BaseModel):
    email: str
    name: Str
    phone: str

class UserRequest(UserBase):
    password: str

    class Config:
        orm_mode = True

class UserResponse(UserBase):
    id: int
    created_at: _datetime.datetime

        class Config:
            orm_mode = True
