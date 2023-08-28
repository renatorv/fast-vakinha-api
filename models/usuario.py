from typing import Optional
from pydantic import BaseModel


class Usuario(BaseModel):
    id: Optional[str] = None 
    name: Optional[str] = None
    email: str
    password: str