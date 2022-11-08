from fastapi import APIRouter

from schemas.users import UserSchema

router = APIRouter(tags=['users'])


@router.get("/users")
async def users(asd: str):
    return [{"user_id": 1}, {"user_id": 2}, {"user_id": 3}, {'asd': asd}]


@router.get("/users/{user_id}")
async def read_user_id(user_id: str):
    return {"user_id": user_id}


@router.post("/users", status_code=201, response_model=UserSchema)
async def add_user(user: UserSchema):
    return user
