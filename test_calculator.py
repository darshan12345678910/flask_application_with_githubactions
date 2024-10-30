import pytest
from app import app
from bs4 import BeautifulSoup

# Configure the test client using the Flask app
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_route(client):
    """Test if the home route loads successfully."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Fun Calculator" in response.data

def test_addition(client):
    """Test addition operation."""
    response = client.post('/calculate', data={'num1': 3, 'num2': 4, 'operation': 'add'})
    assert response.status_code == 200

    # Parse HTML and locate the result by ID
    soup = BeautifulSoup(response.data, 'html.parser')
    result_text = soup.find(id="result").text  # Expected to contain "Result: 7.0"
    assert "Result: 7.0" in result_text

def test_subtraction(client):
    """Test subtraction operation."""
    response = client.post('/calculate', data={'num1': '10', 'num2': '4', 'operation': 'subtract'})
    assert response.status_code == 200

    # Parse HTML and locate the result by ID
    soup = BeautifulSoup(response.data, 'html.parser')
    result_text = soup.find(id="result").text
    assert "Result: 6.0" in result_text

def test_multiplication(client):
    """Test multiplication operation."""
    response = client.post('/calculate', data={'num1': '3', 'num2': '4', 'operation': 'multiply'})
    assert response.status_code == 200

    # Parse HTML and locate the result by ID
    soup = BeautifulSoup(response.data, 'html.parser')
    result_text = soup.find(id="result").text
    assert "Result: 12.0" in result_text

def test_division(client):
    """Test division operation."""
    response = client.post('/calculate', data={'num1': '8', 'num2': '2', 'operation': 'divide'})
    assert response.status_code == 200

    # Parse HTML and locate the result by ID
    soup = BeautifulSoup(response.data, 'html.parser')
    result_text = soup.find(id="result").text
    assert "Result: 4.0" in result_text

def test_division_by_zero(client):
    """Test division by zero handling."""
    response = client.post('/calculate', data={'num1': '8', 'num2': '0', 'operation': 'divide'})
    assert response.status_code == 200

    # Parse HTML and locate the result by ID
    soup = BeautifulSoup(response.data, 'html.parser')
    result_text = soup.find(id="result").text
    assert "Undefined (division by zero)" in result_text
