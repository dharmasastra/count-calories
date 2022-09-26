from pydantic import BaseModel

class KaloriModel(BaseModel):
    gender: str
    age: int
    weight: int
    height: int
    activity: float

