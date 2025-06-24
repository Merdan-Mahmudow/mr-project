from fastapi import FastAPI
from app.routes import router


root = FastAPI()

root.include_router(router=router)
