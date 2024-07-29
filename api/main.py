import os
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from pymongo import MongoClient 

os.environ["MONGO_USERNAME"] =  "NOPE"
os.environ["MONGO_PASSWORD"] = "NOPE"

MONGO_USERNAME = os.environ.get("MONGO_USERNAME")
MONGO_PASSWORD = os.environ.get("MONGO_PASSWORD")

MONGO_CONNECTION_STRING = f"mongodb+srv://{MONGO_USERNAME}:{MONGO_PASSWORD}@main.w7srgez.mongodb.net"

class GetGames(BaseModel):
    sport: Optional[str] | None = None
    open_status: Optional[str] | None = None
    skill_level: Optional[str] | None = None
    date: Optional[str] | None = None
    time: Optional[str] | None = None
    location: Optional[tuple] | None = None
    public_private: Optional[str] | None = None
    num_players: Optional[int] | None = None
    num_open: Optional[int] | None = None
    cost: Optional[int] | None = None
    sort: Optional[str] | None = None
    page_num: Optional[int] | None = 1
    num_result: Optional[int] | None = 10
    byo_equipment: Optional[bool] | None = None

app = FastAPI()

@app.post("/api/get_games")
async def get_games(params: GetGames):
    client = MongoClient(MONGO_CONNECTION_STRING)

    db = client.main
    games = db.games

    query = {}
    if params.sport:
        query["sport"] = params.sport
    if params.open_status:
        query["open_status"] = params.open_status
    if params.skill_level:
        query["skill_level"] = params.skill_level
    if params.public_private:
        query["public_private"] = params.public_private
    if params.num_players:
        query["num_players"] = params.num_players
    if params.num_open:
        query["num_open"] = {"$gte": params.num_open}
    if params.cost:
        query["cost"] = {"$lte": params.cost}
    if params.byo_equipment:
        query["byo_equipment"] = params.skill_level

    found_games = list(games.find(query))
    for game in found_games:
        game['_id'] = str(game['_id'])

    return {"games": found_games}

@app.post("/api/get_user")
async def get_user():
    return

@app.post("/api/get_game")
async def get_game():
    return

@app.post("/api/edit_user")
async def edit_user():
    return

@app.post("/api/create_user")
async def create_user():
    return

@app.post("/api/create_game")
async def create_game():
    return
