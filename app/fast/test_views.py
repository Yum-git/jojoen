from fastapi.testclient import TestClient

from .views import app

client = TestClient(app)


# 日本語文章を入れると
def test_japanese_sentence():
    response = client.get("/api",
        params={"sentence": "吾輩は猫である。"},
    )
    
    assert response.status_code == 200
    assert isinstance(response.json()["audio"], str)
    assert isinstance(response.json()["picture"], str)


# 英語文章を入れると
def test_english_sentence():
    response = client.get("/api",
        params={"sentence": "President Donald Trump found himself trapped in an election riddle of his own making Friday."},
    )
    assert response.status_code == 200
    assert isinstance(response.json()["audio"], str)
    assert isinstance(response.json()["picture"], str)


# 数字を入れると
def test_number_sentence():
    response = client.get("/api",
        params={"sentence": "0"},
    )

    assert response.status_code == 200
    assert isinstance(response.json()["audio"], str)
    assert isinstance(response.json()["picture"], str)


# 何も入れないと
def test_none_sentence():
    response = client.get("/api",
        params={"sentence": ""},
    )

    assert response.status_code == 200
    assert response.json()["audio"] == 'None'
    assert response.json()["picture"] == 'None'


# 記号を入れると
def test_symbol_sentence():
    response = client.get("/api",
        params={"sentence": "!"},
    )

    assert response.status_code == 200
    assert response.json()["audio"] == 'None'
    assert response.json()["picture"] == 'None'


# アラビア語を入れると
def test_arabic_sentence():
    response = client.get("/api",
        params={"sentence": "أنا قطة"},
    )

    assert response.status_code == 200
    assert response.json()["audio"] == 'None'
    assert response.json()["picture"] == 'None'
