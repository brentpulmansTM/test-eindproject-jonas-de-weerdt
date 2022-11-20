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
    "animals": [{"id":0,"name": "badger", "gender": "M"}, {"id":1,"name": "lion", "gender": "F"}, {"id":2,"name": "wolf", "gender": "F"},
                {"id":3,"name": "porcupine", "gender": "M"}, {"id":4,"name": "cheetah", "gender": "M"},
                {"id":5,"name": "giraffe", "gender": "M"},
                {"id":6,"id":7,"name": "panda", "gender": "F"}, {"id":8,"name": "gorilla", "gender": "M"}, {"id":9,"name": "tiger", "gender": "F"},
                {"id":10,"name": "koala", "gender": "F"}, {"id":11,"name": "jaguar", "gender": "M"},
                {"id":12,"name": "elephant", "gender": "M"},
                {"id":13,"name": "blue-and-yellow macaw", "gender": "M"}, {"id":14,"name": "hornbill", "gender": "M"},
                {"id":15,"name": "rhinoceros", "gender": "F"},
                {"id":16,"name": "kangaroo", "gender": "F"}, {"id":17,"name": "ostrich", "gender": "F"},
                {"id":18,"name": "bison", "gender": "M"},
                {"id":19,"name": "wallaby", "gender": "F"}, {"id":20,"name": "badger", "gender": "F"}]
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
    id: int
    name: str
    gender: str
    


@app.post("/animal/create/", response_model=AnimalIn)
def create_animal(animal: AnimalIn):
    return animal
