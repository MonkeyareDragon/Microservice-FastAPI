from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_home_view():
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    
    
def test_post_view():
    response = client.post("/")
    assert response.status_code == 200
    assert "application/json" in response.headers["content-type"]
    assert response.json() == {"message": "Hello, World!"}