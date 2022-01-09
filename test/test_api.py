from fastapi.testclient import TestClient
from src.api import app

client = TestClient(app)


def test_reason():
    """
    Test that the reason endpoint is accepting the right content

    :return: None
    """
    swrl_rule = {
        'name': 'test rule',
        'description': 'Test description',
        'rule': 'test rule'
    }
    ontology = {
        'name': 'test ontology',
        'description': 'Test ontology',
        'ontology': b'test'
    }
    response = client.post("/reason",
                           json={"rules": [swrl_rule], "ontologies": [ontology]},
                           )
    assert response.status_code == 200
