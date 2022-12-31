from pydantic import BaseModel

class User(BaseModel):
    full_name: str
    

class Notification(BaseModel):
    action : str
    full_name: str