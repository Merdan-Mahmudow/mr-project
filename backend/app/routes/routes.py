from fastapi import APIRouter
from app.routes.v1.main import router as V1

router = APIRouter(prefix="/api")

router.include_router(router=V1)
