from fastapi import FastAPI, Query
import random
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "https://localhost",
    "http://localhost:8080",
    "https://jonasdeweerdt.github.io"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=[""],
    allow_headers=[""],
)


all_animals = {
    "animals": [{"name": "badger", "gender": "M"}, {"name": "lion", "gender": "F"}, {"name": "wolf", "gender": "F"},
                {"name": "porcupine", "gender": "M"}, {"name": "cheetah", "gender": "M"},
                {"name": "giraffe", "gender": "M"},
                {"name": "panda", "gender": "F"}, {"name": "gorilla", "gender": "M"}, {"name": "tiger", "gender": "F"},
                {"name": "koala", "gender": "F"}, {"name": "jaguar", "gender": "M"},
                {"name": "elephant", "gender": "M"},
                {"name": "blue-and-yellow macaw", "gender": "M"}, {"name": "hornbill", "gender": "M"},
                {"name": "rhinoceros", "gender": "F"},
                {"name": "kangaroo", "gender": "F"}, {"name": "ostrich", "gender": "F"},
                {"name": "bison", "gender": "M"},
                {"name": "wallaby", "gender": "F"}, {"name": "badger", "gender": "F"}]
}


@app.get("/animal/random")
def random_animal():
    randomnumber = random.randint(0, len(all_animals["animals"]))
    return {"animal": all_animals["animals"][randomnumber-1]}


@app.get("/animal")
def chosen_animal(name: str = Query(default=None, min_length=4, max_length=30),
                  gender: str = Query(default=None, min_length=1, max_length=1)):
    animal_json = {"animals": []}
    for i in range(0, len(all_animals["animals"])):
        if name == all_animals["animals"][i]["name"] or gender == all_animals["animals"][i]["gender"]:
            animal_json["animals"].append(
                {"name": all_animals["animals"][i]["name"], "gender": all_animals["animals"][i]["gender"]})

    return animal_json


class AnimalIn(BaseModel):
    name: str
    gender: str


@app.post("/animal/create/", response_model=AnimalIn)
def create_animal(animal: AnimalIn):
    return animal
