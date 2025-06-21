from fastapi import FastAPI
from app.routes import routes as v1


root = FastAPI()

root.include_router(router=v1.router)
