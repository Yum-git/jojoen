from fastapi.testclient import TestClient

from .views import app

client = TestClient(app)


def test_make_text_to_music():
    response = client.get("/api",
        params={"sentence": "吾輩は猫である。"},
    )
    
    assert response.status_code == 200
    assert isinstance(response.json()["audio"], str)
    assert isinstance(response.json()["picture"], str)