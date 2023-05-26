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


class PlayerPrepareInput(BaseModel):
    cards: List[str]


class Repository:

    def __init__(self):
        self.storage: Dict = {}

    def save(self, game):
        self.storage[game.id] = game

    def find(self, game_id) -> "Game":
        return self.storage.get(game_id)


repo = Repository()


class RoleCard:

    def __init__(self, name):
        self.name = name

    def as_view(self):
        return self.name


class Player:

    # TODO 要有 5 張這回合用的牌
    # TODO 一開始的資源
    # TODO 2 個金塊, 3 種藥材各一

    def __init__(self, player_id):
        self.id = player_id
        self.cards: List[RoleCard] = []

    def add_card_by_name(self, card_name: str):
        # TODO 轉成 Card 物件
        self.cards.append(RoleCard(card_name))

    def as_view(self):
        return dict(player_id=self.id, cards=[x.as_view() for x in self.cards])


class Game:

    # TODO 遊戲準備
    # 3 堆的鍋子
    # 2 堆的櫃子
    # 1 堆的咒語
    # 其他資源：
    # 1. 試管
    # 2. 分剩給玩家剩餘的金塊、藥材。

    def __init__(self):
        # game_created
        # round_started
        self.state = "game_created"
        self.id = "game-9527"
        self.players: List[Player] = []

    def add_player(self, data: PlayerInput):
        # TODO 遊戲人數為 3 ~ 5 人
        self.players.append(Player(data.id))

    def as_view(self):
        players = [dict(id=x.id) for x in self.players]
        return {"game_id": self.id, "state": self.state, "players": players}

    def refresh_state(self):
        # game_created -> all players have prepared -> round_started
        if self.state == "game_created" and len([x for x in self.players if len(x.cards) == 5]) == len(self.players):
            # TODO rules for round_started
            """
            每回合的準備:

            [done] 1. 玩家由手中的 12 張牌, 挑選 5 張作為此回合的牌組。
            [ ] 2. 隨機選擇一位玩家, 作為第一回合起始玩家開始回合。
            [ ] 3. 上一回合的贏家 為回合始起玩家。
            """
            self.state = "round_started"


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


@app.post("/games/{game_id}/player/{player_id}/prepare")
async def prepare_round(game_id: str, player_id: str, prepared_cards: PlayerPrepareInput):
    game = repo.find(game_id)
    player = [x for x in game.players if x.id == player_id][0]

    # TODO exactly 5 cards in the prepared cards
    for card in prepared_cards.cards:
        player.add_card_by_name(card)

    # Aggregate Root
    # Tx bounded
    # State machine
    game.refresh_state()
    repo.save(game)

    return player.as_view()


if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, log_level="info")
