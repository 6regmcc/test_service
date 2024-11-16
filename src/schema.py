from pydantic import BaseModel


class CreateNote (BaseModel):
    note_a: str
    note_b: str