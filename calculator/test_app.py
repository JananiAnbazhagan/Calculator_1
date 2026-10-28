import pytest
from app import app, calculate_grade

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_calculations():
    # Test grade logic (Push 2 feature)
    assert calculate_grade(95) == 'A'
    assert calculate_grade(85) == 'B'
    assert calculate_grade(50) == 'F'

def test_web_flow(client):
    rv = client.post('/', data={'marks': '80, 90, 70'})
    assert b'Total' in rv.data
    assert b'Average' in rv.data
    assert b'Grade' in rv.data # Verifying Push 2 output

from app import app

def test_calculation():
    client = app.test_client()
    response = client.post('/', data={'m1': '80', 'm2': '90', 'm3': '70'})
    assert response.status_code == 200
    assert b"Total Marks: 240.0" in response.data
    assert b"Average Marks: 80.0" in response.data
    assert b"Grade: <strong>A</strong>" in response.data
