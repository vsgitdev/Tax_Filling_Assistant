import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """Test the home page"""
    response = client.get('/')
    assert response.status_code == 200
    assert b"TaxViser" in response.data

def test_submit_invalid_input(client):
    """Test submitting invalid input"""
    response = client.post('/submit', data={'income': 'abc', 'expenses': 'def'})
    assert response.status_code == 302
    assert b"Invalid input" in response.data

def test_submit_valid_input(client):
    """Test submitting valid input"""
    response = client.post('/submit', data={'income': '10000', 'expenses': '5000'})
    assert response.status_code == 302
    assert b"success" in response.headers['Location']
