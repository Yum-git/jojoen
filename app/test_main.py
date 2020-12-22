# from flaskr.views import app
from fastapi.testclient import TestClient
from fast.views import app

# clientTest
client = TestClient(app)


def test_pattern_1_1():
    response = client.get("/api",
        params={"sentence": "吾輩は猫である。"},
    )
    assert response.status_code == 200
    assert isinstance(response.json()["audio"], str)
    assert isinstance(response.json()["picture"], str)


def test_pattern_1_2():
    response = client.get("/api",
        params={"sentence": "President Donald Trump found himself trapped in an election riddle of his own making Friday."},
    )
    assert response.status_code == 200
    assert isinstance(response.json()["audio"], str)
    assert isinstance(response.json()["picture"], str)


def test_pattern_2():
    response = client.get("/api",
        params={"sentence": ""},
    )

    assert response.status_code == 200
    assert response.json()["audio"] == 'None'
    assert response.json()["picture"] == 'None'


def test_pattern_3():
    response = client.get("/api",
        params={"sentence": "!"},
    )

    assert response.status_code == 200
    assert response.json()["audio"] == 'None'
    assert response.json()["picture"] == 'None'

def test_pattern_4():
    response = client.get("/api",
        params={"sentence": "أنا قطة"},
    )

    assert response.status_code == 200
    assert response.json()["audio"] == 'None'
    assert response.json()["picture"] == 'None'
