from typing import List

from fastapi import FastAPI
from .Ontology import Ontology
from .Rule import Rule

app = FastAPI(title="SWRL Server",
              description="An API endpoint for processing SWRL rules",
              version="0.0.1")


@app.post("/reason")
def reason(rules: List[Rule], ontologies: List[Ontology]):
    """
    Takes a set of SWRL rules and ontology files and runs the reasoner with them.

    :param rules: The SWRL rules that will be applied across the ontology
    :param ontologies: A set of ontologies that the SWRL rules are run over
    :return: Structured information about the result from the processing
    """
    return 1
