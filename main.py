from fastapi import FastAPI
import uvicorn
from creature import Creature, Ability

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/v1/creatures/")
async def creatures():
    all_creatures = Creature.objects()

    list_of_all_creatures = [each_creature.to_mongo().to_dict() for each_creature in all_creatures]

    for each_entry in list_of_all_creatures:
        del each_entry["_id"]
        del each_entry["ability"]

    return list_of_all_creatures


if __name__ == '__main__':
    uvicorn.run(app, port=5010)
