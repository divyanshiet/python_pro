from pydantic import BaseModel, Field

class Student(BaseModel):
    name: str = Field(min_length=1)
    marks: int = Field(ge=0, le=100)