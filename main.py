from fastapi import FastAPI

from routers import main_router

app = FastAPI(debug=True, version='0.0.1')

app.include_router(main_router)
q