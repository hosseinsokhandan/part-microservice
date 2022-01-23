from pydantic import BaseModel


class PartInSchema(BaseModel):
    name: str
    automobile_id: int

class PartOutSchema(BaseModel):
    id: int
    name: str
    automobile_id: int
