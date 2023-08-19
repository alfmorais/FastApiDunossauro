from fastapi.testclient import TestClient

from fast_zero.app import app

client = TestClient(app)


def test_root_success(client=client):
    expected_result = {'message': 'Olá Mundo!'}

    response = client.get('/')

    assert response.status_code == 200
    assert response.json() == expected_result
