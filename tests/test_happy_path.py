from starlette.testclient import TestClient

from main import app


def test_happy_path():
    client = TestClient(app)

    #
    # Game created
    #

    request_body = {"players": [
        {"id": "player-1"},
        {"id": "player-2"},
        {"id": "player-3"},
    ]}
    response = client.post("/games", json=request_body)

    assert response.status_code == 200

    expected = {"game_id": "game-9527", "players": [
        {"id": "player-1"},
        {"id": "player-2"},
        {"id": "player-3"},
    ]}
    assert response.json() == expected

    #
    # Game look up
    #
    response = client.get("/games/game-9527")
    expected = {"game_id": "game-9527", "players": [
        {"id": "player-1"},
        {"id": "player-2"},
        {"id": "player-3"},
    ]}
    assert response.json() == expected
