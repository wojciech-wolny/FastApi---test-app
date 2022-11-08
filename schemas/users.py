from pydantic import BaseModel


class UserSchema(BaseModel):
    username: str
    full_name: str | None = None