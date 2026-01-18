from __future__ import annotations

from fastapi import APIRouter, HTTPException, status

from .models import Item
from .schemas import ItemCreate, ItemOut

router = APIRouter(prefix="/items", tags=["items"])

# In-memory store (OK for demo)
_items: dict[int, Item] = {}
_next_id = 1


@router.get("", response_model=list[ItemOut])
def list_items() -> list[ItemOut]:
    return [ItemOut(id=i.id, name=i.name, description=i.description) for i in _items.values()]


@router.post("", response_model=ItemOut, status_code=status.HTTP_201_CREATED)
def create_item(payload: ItemCreate) -> ItemOut:
    global _next_id
    item = Item(id=_next_id, name=payload.name, description=payload.description)
    _items[item.id] = item
    _next_id += 1
    return ItemOut(id=item.id, name=item.name, description=item.description)


@router.get("/{item_id}", response_model=ItemOut)
def get_item(item_id: int) -> ItemOut:
    item = _items.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return ItemOut(id=item.id, name=item.name, description=item.description)


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int) -> None:
    if item_id not in _items:
        raise HTTPException(status_code=404, detail="Item not found")
    del _items[item_id]
