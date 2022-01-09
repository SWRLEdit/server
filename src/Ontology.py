from pydantic import BaseModel


class Ontology(BaseModel):
    name: str
    description: str
    ontology: bytes
