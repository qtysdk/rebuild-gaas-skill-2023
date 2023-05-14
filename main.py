from typing import Dict, List, Union

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/walking_skeleton")
async def read_root():
    return {"Walking": "Skeleton"}


class PlayerInput(BaseModel):
    id: str


class CreateGameInput(BaseModel):
    players: List[PlayerInput]


class Repository:

    def __init__(self):
        self.storage: Dict = {}

    def save(self, game):
        self.storage[game.id] = game

    def find(self, game_id) -> "Game":
        return self.storage.get(game_id)


repo = Repository()


class Player:

    # TODO 要有 5 張這回合用的牌
    # TODO 一開始的資源
    # TODO 2 個金塊, 3 種藥材各一

    def __init__(self, player_id):
        self.id = player_id


class Game:

    # TODO 遊戲準備
    # 3 堆的鍋子
    # 2 堆的櫃子
    # 1 堆的咒語
    # 其他資源：
    # 1. 試管
    # 2. 分剩給玩家剩餘的金塊、藥材。

    def __init__(self):
        self.id = "game-9527"
        self.players: List[Player] = []

    def add_player(self, data: PlayerInput):
        # TODO 遊戲人數為 3 ~ 5 人
        self.players.append(Player(data.id))

    def as_view(self):
        players = [dict(id=x.id) for x in self.players]
        return {"game_id": self.id, "players": players}


# Web (HTTP Client)
# Controller (寫你的 API)
@app.post("/games")
async def create_game(request_body: CreateGameInput):
    game = Game()
    for data in request_body.players:
        game.add_player(data)

    # TODO 需要符合遊戲規則 3 ~ 5 人
    # game.start()

    repo.save(game)
    return game.as_view()


@app.get("/games/{game_id}")
async def look_up_game(game_id: str):
    game = repo.find(game_id)
    return game.as_view()


if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, log_level="info")
