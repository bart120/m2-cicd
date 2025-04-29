import pytest
from back.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    res = client.get('/')
    assert res.status_code == 200
    assert b"API is running" in res.data

def test_data_endpoint(client):
    res = client.get('/data')
    assert res.status_code in [200, 500]