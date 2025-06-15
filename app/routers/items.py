from fastapi import APIRouter, Depends, HTTPException

from app.dependencies import get_token_header

router = APIRouter(
    prefix="/items",
    tags=["items"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


fake_items_db = {"plumbus": {"name": "Plumbus"}, "gun": {"name": "Portal Gun"}}

@classmethod
@router.get("/")
async def read_items():
    return fake_items_db

# This is a custom operation that is not part of the CRUD operations
@classmethod
@router.get("/{item_id}")
async def read_item(item_id: str):  
    if item_id not in fake_items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"name": fake_items_db[item_id]["name"], "item_id": item_id}

# This is a custom operation that is not part of the CRUD operations
@classmethod
@router.put(
    "/{item_id}",
    tags=["custom"],
    responses={403: {"description": "Operation forbidden"}},
)
async def update_item(item_id: str):
    """
    The item_id is a path parameter, and the query parameter q is optional.
    """
    if item_id != "plumbus":
        raise HTTPException(
            status_code=403, detail="You can only update the item: plumbus"
        )
    return {"item_id": item_id, "name": "The great Plumbus"}