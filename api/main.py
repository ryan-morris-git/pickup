import os
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from pymongo import MongoClient 
from fastapi.middleware.cors import CORSMiddleware

os.environ["MONGO_USERNAME"] =  "NOPE"
os.environ["MONGO_PASSWORD"] = "NOPE"

MONGO_USERNAME = os.environ.get("MONGO_USERNAME")
MONGO_PASSWORD = os.environ.get("MONGO_PASSWORD")

origins = [
    "http://localhost",
    "http://localhost:3000",
]

MONGO_CONNECTION_STRING = f"mongodb+srv://{MONGO_USERNAME}:{MONGO_PASSWORD}@main.w7srgez.mongodb.net"

class GetTraining(BaseModel):
    sport: Optional[str] | None = None
    location: Optional[str] | None = None
    public_private: Optional[str] | None = None
    cost: Optional[int] | None = None
    sort: Optional[str] | None = None
    page_num: Optional[int] | None = 1
    num_result: Optional[int] | None = 10

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/get_training")
async def get_games(params: GetTraining):
    client = MongoClient(MONGO_CONNECTION_STRING)

    db = client.main
    games = db.lessons

    query = {}
    if params.sport:
        query["sport"] = params.sport
    if params.public_private:
        query["public_private"] = params.public_private
    if params.location:
        query["location"] = params.location
    if params.cost:
        query["cost"] = {"$lte": params.cost}

    found_games = list(games.find(query))
    for game in found_games:
        game['_id'] = str(game['_id'])

    return found_games

@app.post("/api/get_user/{id}")
async def get_user(id: str):
    return

@app.post("/api/get_game/{id}")
async def get_game(id: str):
    return

@app.post("/api/edit_user/{id}")
async def edit_user(id: str):
    return

@app.post("/api/create_user")
async def create_user():
    return

@app.post("/api/create_game")
async def create_game():
    return
