from fastapi import APIRouter
from app.models.user import User #Import le modele User

router = APIRouter()

@router.get("/user")
async def read_users():
    return {"users" : [User(id=1, username="user1", email="user1@example.com"),
             User(id=2, username="user2", email="user2@example.com")]}
 

@router.get("/")
async def root():
    return {"message": "hello world"}

@router.post("/")
def post(user_id: int):
    return {"message": "hello from the post route"}

@router.put("/")
async def put():
    return {"message": "hello from the put route"}

@router.get("/items")
async def list_items():
    return {"message":"List items route"}

@router.get("/items/{item_id}")
async def get_item(item_id:int):
    return {"item":item_id}