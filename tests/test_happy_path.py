from starlette.testclient import TestClient

from main import app


def test_happy_path():
    client = TestClient(app)

    #
    # Game created
    #

    other_players_request_body = {"players": [
        {"id": "player-1"},
        {"id": "player-2"},
        {"id": "player-3"},
    ]}
    response = client.post("/games", json=other_players_request_body)

    assert response.status_code == 200

    expected = {"game_id": "game-9527", "state": "game_created", "players": [
        {"id": "player-1"},
        {"id": "player-2"},
        {"id": "player-3"},
    ]}
    assert response.json() == expected

    #
    # Game look up
    #
    response = client.get("/games/game-9527")
    expected = {"game_id": "game-9527", "state": "game_created", "players": [
        {"id": "player-1"},
        {"id": "player-2"},
        {"id": "player-3"},
    ]}
    assert response.json() == expected

    #
    # Players prepare their round
    #

    initial_player_request_body = {
        "cards": [
            "card-1", "card-2", "card-3", "card-4", "card-5"
        ]
    }

    other_players_request_body = {
        "cards": [
            "card-6", "card-2", "card-3", "card-4", "card-5"
        ]
    }

    response = client.post('/games/game-9527/player/player-1/prepare', json=initial_player_request_body)
    expected = {"player_id": "player-1", "cards": [
        "card-1", "card-2", "card-3", "card-4", "card-5"
    ]}
    assert response.status_code == 200
    assert response.json() == expected
    check_game_state(client, "game_created")

    response = client.post('/games/game-9527/player/player-2/prepare', json=other_players_request_body)
    expected = {"player_id": "player-2", "cards": [
        "card-6", "card-2", "card-3", "card-4", "card-5"
    ]}
    assert response.status_code == 200
    assert response.json() == expected
    check_game_state(client, "game_created")

    response = client.post('/games/game-9527/player/player-3/prepare', json=other_players_request_body)
    expected = {"player_id": "player-3", "cards": [
        "card-6", "card-2", "card-3", "card-4", "card-5"
    ]}
    assert response.status_code == 200
    assert response.json() == expected
    check_game_state(client, "round_started")


def check_game_state(client, expected_state: str):
    response = client.get("/games/game-9527")
    expected = {"game_id": "game-9527", "state": expected_state, "players": [
        {"id": "player-1"},
        {"id": "player-2"},
        {"id": "player-3"},
    ]}
    assert response.json() == expected
