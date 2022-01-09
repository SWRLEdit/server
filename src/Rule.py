from pydantic import BaseModel


class Rule(BaseModel):
    name: str
    description: str
    rule: str
