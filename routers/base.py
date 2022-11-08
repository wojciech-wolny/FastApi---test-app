from fastapi import APIRouter, Body

from schemas.items import ItemSchema

router = APIRouter(tags=['base'])

items = []


@router.get('/hello')
async def hello(name: str = None):
    if name:
        return {'msg': f'Hello {name}'}
    return {'msg': 'hello world!'}


@router.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id < len(items):
        return items[item_id]
    return {}


@router.post("/items", status_code=201)
async def create_item(item: ItemSchema):
    items.append(item)
    return item


@router.get("/items")
async def read_items():
    return items


@router.put("/items/{item_id}")
async def read_item(item_id: int, item: ItemSchema = Body(embed=True)):
    if item_id < len(items):
        items[item_id] = item
    results = {"item_id": item_id, "item": item}
    return results
