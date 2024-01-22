from fastapi import FastAPI

app = FastAPI()
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Caz"}, {"item_name": "Daz"}]

@app.get("/items/")
async def read_item(idx: int = 0, max: int = 3):
    print("--------------------------------------")
    print("we read all items in a python dict")
    print("--------------------------------------")
    return fake_items_db[idx : idx + max]