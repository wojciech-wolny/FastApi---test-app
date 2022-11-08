from fastapi import APIRouter

from routers import users
from routers import base
from routers import enum_as_schema

main_router = APIRouter()
main_router.include_router(base.router)
main_router.include_router(enum_as_schema.router)
main_router.include_router(users.router)
