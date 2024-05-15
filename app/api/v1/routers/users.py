from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_users():
    return {"users": ["user1", "user2"]}

@router.get("/{user_id}")
def read_user(user_id: int):
    return {"user_id": user_id, "name": f"user{user_id}"}