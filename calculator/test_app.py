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
