from fastapi import FastAPI
import uvicorn
from creature import Creature, Ability

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/v1/creatures/")
async def creatures(page: int = 0, items_per_page: int = 8):
    all_creatures = Creature.objects()[page * items_per_page:page * items_per_page + items_per_page]

    list_of_all_creatures = [each_creature.to_mongo().to_dict() for each_creature in all_creatures]

    for each_entry in list_of_all_creatures:
        del each_entry["_id"]
        del each_entry["ability"]

    return list_of_all_creatures


@app.get("/v1/abilities/")
async def abilities(page: int = 0, items_per_page: int = 8):
    all_abilities = Ability.objects()[page * items_per_page:page * items_per_page + items_per_page]

    list_of_all_abilities = [each_ability.to_mongo().to_dict() for each_ability in all_abilities]

    for each_entry in list_of_all_abilities:
        del each_entry["_id"]

    return list_of_all_abilities


if __name__ == '__main__':
    uvicorn.run(app, port=5010)
