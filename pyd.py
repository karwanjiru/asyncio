#Pydantic - a data validation library in python
#Benefits - IDE() Type Hints, Data Validation, JSON Serialization

from pydantic import BaseModel, EmailStr, field_validator

class User(BaseModel):
    name : str
    email : EmailStr
    account_id : int

    @field_validator("account_id")
    def validate_account_id(cls,value):
        if value <= 0:
            raise ValueError(f"Account_id must be positive: {value}")
        return value

user = User(
    name = "Diana",
    email = "karwanjiru@gmail.com",
    account_id = 1001
)

#unpacking a dict
#user = User(**user_data)

print(user.name)
print(user.email)
print(user.account_id)

#To convert a pydantic model to JSON, returns a JSON string representation of model's data 
user_json_str = user.model_dump_json()
print(user_json_str)

#If you want a plain python dict not JSON str
user_json_obj = user.model_dump() 
print(user_json_obj)

#JSON str back to pydantic model
user = User.model_validate_json(user_json_str)
print(user)


